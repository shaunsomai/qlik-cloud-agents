---
source: https://qlik.dev/manage/reports/
last_updated: 2025-07-08T16:09:30Z
---

# Overview

In Qlik Cloud, users are provided methods for generating reporting output in various
formats, such as:

- [Tabular reporting](#tabular-reporting): Highly customizable Excel tabular
  reports, which can be scheduled and governed
- [In-app exports](#in-app-exports): In-app, on-demand, user-based exports
  - Snapshots of Qlik Sense sheets or charts, in PNG or PDF format
  - Excel exports from Qlik Sense charts
  - Compositions of objects from within a Qlik Sense app
- [Hypercube exports](#hypercube-exports): Direct exports from the Qlik
  Sense engine via API calls

## Tabular reporting

Tabular reporting enables Qlik Cloud customers to address common operational report
distribution requirements, such as providing:

- Custom and highly formatted Excel documents from Qlik data and Qlik visualizations
- Paginated tables of sales/transactional data
- Repeated sheets of departmental analysis

Report developers can author report templates leveraging data and visualizations from
a Qlik Sense application, from the familiarity of Microsoft Office 365 using Add-in technology.

![tabular reporting example showing a formatted table of data in Excel](https://qlik.dev/_astro/tabular-reporting-example.ZBSx_HEH.png)

Once the template is ready, there is in-app control of:

- Report tasks - defining the criteria for when reports are generated
- Distribution lists and folders - managing both internal and external recipients of
  generated reports
- Filters - applying selections per recipient, group, or report task

To learn how to configure reports using the user interface, see the [Tabular Reporting documentation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/cloud-tabular-reports-intro.htm)
on Qlik Help.

To learn how to programmatically deploy Tabular Reports between spaces or tenants, see [Deploy Tabular Reports](https://qlik.dev/manage/reports/deploy-tabular-reports).

## In-app exports

If you're looking to export sheets, objects, or compositions of objects on demand,
the Qlik Sense interface provides methods for users to request on-demand exports. It is
also possible for users to create compositions using the Reporting Service connector
in Qlik Automate.

Some of this capability is also available through the [Reports API](https://qlik.dev/apis/rest/reports).
You can use it to export compositions, images, or sheets.

Learn more with the [generate reports using Reporting API tutorial](https://qlik.dev/embed/reports/reporting-api-samples/).

## Hypercube exports

Qlik Sense provides APIs and toolkits for accessing the underlying data in app
data models directly. To learn more about the overall capability, review
the [embedding tutorials and topics](https://qlik.dev/embed), or look at
the Qlik Sense [JSON-RPC QIX API](https://qlik.dev/apis/json-rpc/qix) to dive right
in.
