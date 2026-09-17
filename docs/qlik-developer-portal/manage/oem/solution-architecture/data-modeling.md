---
source: https://qlik.dev/manage/oem/solution-architecture/data-modeling/
last_updated: 2026-05-27T18:16:42+01:00
---

# Data modeling

Data modeling is the foundation of the consumer analytics experience served by your Qlik Cloud deployment. Unlike
traditional SQL-based platforms that require
complex query optimization, Qlik Cloud's associative model simplifies data relationships while providing superior
performance and flexibility for consumers.

## Why data modeling matters

The Qlik Sense in-memory engine loads your data at reload time and holds it resident in memory.
The shape and size of that in-memory model determines whether your apps reload within time and
memory limits, how fast charts respond to user selections, and how soon users
can interact with the apps from a cold start. A well-structured model does more with less: it loads fast,
stays within
subscription tier limits, and responds consistently regardless of user load - without any
database infrastructure to scale.

In an OEM context, data modeling decisions also govern security. Whether you isolate each
customer's data in a separate app or separate it within a shared app using section access
determines both the security boundary and the customization options you can offer. A separate
app per customer provides complete data isolation enforced at the infrastructure level; section
access in a shared app provides row-level data filtering but all customers share the same
application structure, making it difficult to offer self-service analytics
creation for all end users.

## Data modeling approaches

### Template-based per-customer models (recommended)

A template application defines the base load script, data model, and visualizations. Automated
deployment creates a customer-specific instance from that template and populates it with the
customer's actual data at reload time. Each customer's app is fully isolated: separate data,
separate in-memory state, separate space.

This is the standard pattern for OEM deployments because it provides complete data isolation
without relying on row-level filtering, supports per-customer customization (different regions,
different feature sets, different data sources), and meets standard compliance requirements. It
also simplifies operations: you monitor, audit, and roll out changes to customers independently.
A staged rollout - updating a canary set of tenants first, validating, then extending to all
tenants - is straightforward because each customer's deployment is a separate unit.

The automation overhead is higher than a single-app approach, but that overhead pays for itself:
updates to the template are deployed to each customer on your schedule rather than all at once,
and a problem with one customer's data does not affect any other customer.

### Single model with logical separation (not recommended for most cases)

One Qlik Sense application holds all customers' data. Section access configuration reduces what
each user or customer can see at row level - a customer's users are limited to their own records -
but all customers share the same application structure, the same sheets, and the same published
content. Any content an author publishes is accessible to all users with view
permissions on the application.

This approach minimizes the number of apps to maintain, and a single change applies immediately
across all customers. The limitations are significant, however: all customers must have identical
data structures, no per-customer customization of the application is possible, and compliance or
data sovereignty requirements often prohibit placing multiple customers' data in the same application.
Section access requires careful configuration - misconfiguration risks data exposure across customers.
This option is appropriate for simple, anonymous analytics with no personal data
and a small, homogeneous customer base.

## Modeling for performance

Qlik Sense runs on an in-memory engine, so the shape, volume, and structure of your data model have a direct impact on
both reload success and user responsiveness. On Qlik Cloud's standard tiers, apps must stay within 5, 10, or 15 GB
in-memory (depending on subscription tier) to be openable without Large App capacity. Exceeding that typically requires
you to use a space with Large App support, or move to a higher subscription tier with a higher standard limit.

The memory limit is per app, not aggregate. An efficient app that stays well within its tier's ceiling costs nothing
extra to run - and you can open as many of them in parallel as your user base demands, all within the same subscription.
In an OEM deployment with hundreds or thousands of per-customer app instances, this is significant: a lean model that
would have cost you nothing at ten customers still costs nothing at ten thousand. The practices in this section are how
you keep models in that range.

### Design with tier limits in mind

- **Know your app memory ceiling**: Be aware of the memory limits in your subscription. Memory limits are simply a
  guardrail,
  and apply per app rather than in aggregate. Monitor your app's in-memory size after reloads and track growth over
  time.
- **Iterative growth vs big monoliths**: Start simple; avoid overloading an app early. If usage patterns or data volume
  grow, refactor incrementally.
- **Graceful overflow**: If an app is nearing limit, consider offloading older data to summary models or
  migrating to Large App space as necessary.

### Data partitioning and sharding (chunking)

- **Time partitioning**: Split large fact tables into monthly, quarterly, or yearly partitions (for example, Fact\_2026,
  Fact\_2025,
  etc.) in files to improve refresh and data load performance. Load recent partitions in detail, archive older
  partitions
  or rely on summaries.
- **Tenant / customer isolation**: In multi-tenant scenarios, implement separate apps and separate data partitions per
  customer. This keeps data refreshes fast and controllable.
- **Data layering / chained data files**: Build a multi-layer architecture where possible to divide up complex workloads
  1. Raw data (mirror of source)
  2. Cleaned / standardized data
  3. Business data (with derived fields, denormalized)
- **Incremental data updates**: Do not rebuild entire data files if only incremental data changes. Use delta logic,
  change capture, insertion/deletion detection.

### 3. Schema and association design

- **Prefer simple star schemas**: One large fact tables and dimension tables is ideal. Avoid deep snowflake
  (multi-hop junctions) unless justified.
- **Avoid synthetic keys by design**: If two tables share multiple fields, Qlik auto-generates synthetic link tables.
  Resolve by:
  - Renaming fields to disambiguate
  - Creating a link (junction) table
  - Using `ApplyMap()` or mapping loads instead of full joins
  - Concatenating tables when appropriate
- **Remove circular references**: Detect and break circles (for example, dropping one field, merging tables, or using a
  link table)
- **Minimize composite / concatenated keys**: Use surrogate keys created during load when necessary,
  rather than carrying multiple text keys.
- **Control high-cardinality fields**: Be cautious of fields with millions of distinct values (for example, free text,
  GUIDs, tokens, timestamps at millisecond precision) as they bloat symbol tables.
- **Use link tables for complex many-to-many**: If many-to-many relationships are needed, a well-designed link table or
  bridge table can help without bloating the model.

### 4. Load script & QVD strategies

- **Prune early**: In your SQL or initial load, select only columns you need; push filtering to the source if possible.
  Avoid `SELECT *`.
- **Leverage database engines**: Offload complex joins, aggregations, or calculations to the database (push-down SQL)
  when you can. Qlik becomes a consumer of clean data in the format needed for the model.
- **Use `ApplyMap()` / mapping loads**: Instead of joining a dimension to a fact table for a single field, map or
  lookup it. This reduces join cost and model bloat.
- **Avoid nested loops / joins in script**: These are harder to maintain and are slower to run and consume
  more memory
  during reload.
- **Incremental load logic**:
  - Use timestamp or numeric keys for delta detection
  - Flag “deleted” or “inactive” rows to support soft deletes
  - Merge or reconcile updates rather than appending rows without checking for duplicates
- **QVD layering and chaining**: Having intermediate QVDs means downstream apps reuse them and avoid repeating
  transformations.
- **Compression and deduplication awareness**: Watch out for fields with many distinct values which hamper
  deduplication;
  large text fields hamper compression.

### 5. Memory and field management

- **Strict field selection**: Only load fields you will use in analysis (dimensions, measures, filters).
- **Drop / unqualify unused fields early**: Immediately drop helper or technical fields not needed downstream.
- **Replace strings with numeric codes**: Use numeric keys or flags rather than storing verbose strings when possible.
- **Aggregate or bin detailed continuous values**: If you have high-granularity numeric data (for example, granular
  timestamps), consider bucketing or rounding if the business allows.
- **Split large text / description fields**: If needed, move them to separate dimension tables (or use document linking)
  and avoid embedding in heavy fact records.

### Expressions, measures, and UI objects

Expressions are how you define what users interact with in apps, and understanding how these are processed will help you
build the best performance for your consumers. Not all expressions are created equal.

Design expressions so the engine can filter first, aggregate later, in parallel, over a small, well-indexed working set.
Anything that makes Qlik evaluate record-by-record or build huge intermediate hypercubes negates multi-threading and
inflates memory use.

#### Understanding Qlik's expression evaluation

The Qlik associative engine (QIX) evaluates expressions in two stages. First, determining which records qualify (logical
state), and then aggregating results. Understanding this distinction is key to writing efficient front-end logic.

**How Qlik calculates expressions:**

- **Associative indexing**: When a user makes selections or a set modifier filters data, QIX resolves the result set
  through its logical index; it doesn't scan every record. This index resolution is highly parallelized and cached.
- **Aggregation phase**: Once the subset is known, QIX splits the data into internal segments (buckets) that are
  processed in parallel across CPU cores. Aggregations like Sum(), Avg(), and Count() are distributed and merged
  efficiently.
- **Row-by-row evaluation**: Functions that must inspect every record (for example, If(), Match(), WildMatch(), or
  nested Aggr() constructs) force the engine to materialize more data before aggregation. This disrupts caching and can
  collapse into single-threaded work for that expression or object.

**Best practices for expression optimization:**

- **Pre-calculate static metrics in script**: If a metric doesn't change with user selection, derive it in the load.
- **Set analysis over `If()`**: `If()` within aggregation can be expensive; set analysis is often faster and more
  cache-friendly. Replace conditional logic inside aggregations (`If(Status='Closed', Sales)`) with set analysis
  (`Sum({<Status={'Closed'}>} Sales)`) to let QIX apply associative filters before scanning records.
- **Avoid nested `Aggr()` where possible**: If you must use `Aggr()`, limit domain size or pre-aggregate. Minimize
  nested `Aggr()` layers; pre-aggregate in the load script or use simplified master measures.
- **Filter dimensions before aggregation**: Use set analysis or calculated dimensions to limit the data domain a chart
  has to process.
- **Use calculation conditions**: For heavy charts, require the user to make a selection (for example,
  `GetSelectedCount(Field)= 1`) before rendering. Apply calculation conditions on heavy charts so objects don't render
  large hypercubes until a selection reduces scope.
- **Measure reuse / variables**: Define core metrics as master measures or variables to avoid duplication and ensure
  consistency. This also has a cache impact since even a small difference in how an expression is written may mean the
  cache can't be used. Keep expressions simple and re-use variables or master items; repeated complex expressions
  prevent cache reuse and trigger redundant computation.
- **Object count management**: Don't overcrowd sheets with dozens of charts; each object will need calculation time.
- **Leverage caching**: Qlik engine caching is more effective when the same expressions/dimensions repeat across
  objects.

**Controlling memory expansion:**

- Every distinct value creates an entry in the symbol table. High-cardinality fields, especially large text or GUIDs,
  inflate memory.
- Row-level functions that return intermediate tables (`Aggr()`, `If()`) can force temporary in-memory expansion of
  millions of rows. Pre-compute flags or summary fields in the load script instead.
- Limit visible dimensions in charts and use top-N or rank filters to shrink hypercubes.
- Avoid loading or aggregating over wide tables with unnecessary fields; each extra symbol set multiplies potential
  cross-combinations the engine must hold.
- Avoid calculated dimensions that perform per-row logic; prefer pre-derived fields in the model.

### Reload and connection optimization

- **Parallelize where safe**: If loading from multiple independent sources, parallelize, but avoid overloading the
  system.
- **Stagger reload schedules**: Don't reload multiple heavy apps at exactly the same time if they share underlying
  sources.
- **Minimize remote calls**: API/web/connector calls are slow; cache in data files in the tenant when possible for
  larger
  data sets.
- **Reuse connections in script**: Do not open and close the same database connection inside a loop.
- **Validate source performance**: On your database, ensure indexes, partitions, and query plans are optimal.
- **Monitor reload duration & memory peaks**: Use logging, the Reload Analyzer, or telemetry to detect reload duration
  issues or memory spikes.

### Multi-tenant and security design

- **App vs row-level filtering strategy**: Decide early whether each tenant gets its own app or whether a single app
  filters by user context (section access).
- **Section Access in script**: Implement row-level security during load; filter data as early as possible.
- **Cross-tenant insights via summary apps**: If you need cross-tenant aggregations, build a summary or “roll-up” app
  rather than embedding it in every tenant's app.
- **Govern resource usage**: Monitor memory usage per tenant, reload durations, and user workloads.

### Monitoring, testing and troubleshooting

- **Instrumentation & telemetry**: Use Qlik's monitoring apps (App Analyzer, Reload Analyzer, App evaluation) to observe
  actual memory footprint and bottlenecks.
- **Incremental testing**\
  After each incremental change, reload and re-measure app size and object rendering time with an app evaluation; don't
  wait until everything is finished.
- **Use performance baselines**: Maintain historical benchmarks (memory, reload time, user load) to detect regressions.
- **Common symptoms & fixes**:
  - *“Request exceeds memory limit” errors during reload or object rendering* → likely your app or object is too large;
    prune fields, reduce hypercube size, or move to large app space.
  - *Unexpected memory growth* → look for fields you forgot to drop, loops generating many intermediate values,
    cartesian products, or synthetic keys.
  - *Slow reload sections* → tune SQL, index sources, push filtering upstream.
  - *Charts failing / blank object* → because object hypercube memory exceeds engine limits; apply calculation
    conditions,
    reduce complexity, or move to a large app space.

### Checklist and best practice reminders

- [ ] Did I load only the fields I need?
- [ ] Did I drop unused fields/tables immediately?
- [ ] Are there synthetic keys or circular references?
- [ ] Are high-cardinality fields controlled?
- [ ] Did I push heavy logic upstream (in source DB) where possible?
- [ ] Are QVDs layered and reused, not duplicated?
- [ ] Are heavy metrics pre-calculated when safe?
- [ ] Are expressions written to leverage how the Qlik engine works?
- [ ] Are object rendering conditions in place?
- [ ] Are reloads scheduled smartly and resource usage monitored?
- [ ] Do I have app evaluations as part of my development process for performance insight?
- [ ] Have I documented my modeling decisions (why fields were dropped, partitioning logic, exceptions) for future you?

## Next steps

**Ready to continue?** → [Data architecture](https://qlik.dev/manage/oem/solution-architecture/data-architecture/)
