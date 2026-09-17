---
source: https://qlik.dev/manage/oem/solution-architecture/brand-customize/
last_updated: 2026-05-27T18:16:42+01:00
---

# Brand Qlik Cloud

This section explores the various ways that you can brand and otherwise customize
your tenant and apps to better align with your company UI and UX.

> **Note:** Avoid CSS overrides and DOM manipulation on Qlik Cloud experiences.
> Unless they are documented in the Product Documentation, they are
> unsupported and may break at any time.
> Please add requests for additional customization options to the [Ideation portal](https://community.qlik.com/t5/Ideation/ct-p/qlik-product-insight).

## What to consider when branding

From an experience perspective, it's important to control the look and feel of your
applications to ensure a consistent and coherent flow for your users. If you have
a design pattern, you can opt to incorporate elements such as:

- Logo set: brand or product logos in various sizes:
  - Favicon: replaces the Qlik icon in the client's browser.
  - Platform navigation logo: replaces the Qlik logo at the top left in most platform experiences.
  - Qlik Sense app logo: either a blank or branded image to be shown
    when the user navigates apps. For more information, see [Changing the thumbnail of an app](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/change-thumbnail-app.htm)
    on Qlik Help.
  - Qlik Sense sheet/story logo: either a blank or branded image to be shown
    when the user navigates within apps.
- Color palette: a set of brand colors for use in Qlik Sense app themes, and in
  Qlik Sense app overviews.
- Imagery and backgrounds: can be used in Qlik Sense apps, particularly with
  the layout container object for custom layouts and visuals.
- Icons: for use in Qlik Sense apps, as well as in the Qlik Cloud hub for generic
  links, and optionally application icons.
- Fonts: Qlik Sense supports a range of fonts, as well as custom fonts through
  themes.

## Branding options for native and embedded experiences

Some options may be valid for only certain [access patterns](https://qlik.dev/manage/oem/solution-architecture/access-route),
such as via native usage of Qlik Cloud, while some might only be available via
specific embedding frameworks:

| Branding option                            | Enhances native experience | Enhances embedded experience |
| ------------------------------------------ | -------------------------- | ---------------------------- |
| Apply a brand to the tenant                | ✔                          | ✖️1                          |
| Curate the hub layouts and content         | ✔                          | ✖️                           |
| Configure per-user preferences             | ✔                          | ✔2                           |
| Remove access to features and capabilities | ✔                          | ✔2                           |
| Style Qlik Sense apps                      | ✔                          | ✔3                           |
| Use your own Identity Provider             | ✔                          | ✖️4                          |

1. The only benefit is when embedding the entire sheet with the legacy iframe embed framework,
   which shows the Qlik Sense top bar. Other frameworks don't show the top bar.
2. Doesn't apply in the default mode when using native chart frameworks such as nebula, or when using
   qlik-embed with `analytics/sheet` and `analytics/chart`, as these do not show context menus and
   experiences found in the Qlik Sense experience. Setting `preview="true"` on the web component enables
   the native context menu and the broader Qlik Sense interaction experience. See
   [UI parameters](https://qlik.dev/embed/qlik-embed/parameters/) for details.
3. Styling support is limited in the default mode when using native chart frameworks such as nebula, or when
   using qlik-embed with `analytics/sheet` and `analytics/chart`. Setting `preview="true"` enables full
   theme matching and support for legacy chart types and visualization extensions. See
   [UI parameters](https://qlik.dev/embed/qlik-embed/parameters/) for details.
4. Apply in scenarios where you use OAuth SPA authentication and a redirect
   to the identity provider is required during the login flow.

## Apply a brand to the tenant

You can apply a tenant-level brand using the [Brands API](https://qlik.dev/apis/rest/brands/),
which considerably reduces the visibility of Qlik branding.

![Direct access to the Qlik Cloud Hub, highlighting the change in logo](https://qlik.dev/_astro/brand-hub-logo.DhO6LKZ7.png)

This allows you to:

- Replace the tenant Qlik logo with your own logo.
- Replace the tenant favicon with your own favicon.
- Remove the visible Qlik Analytics branding when opening apps.
- Remove Qlik Cloud and Qlik Sense branding from the browser title bar.

Qlik branding will still appear in the following places:

- Emails sent by the platform to users (with the exception of emails sent via
  tabular reporting or Qlik Automate).
- In the My Qlik and Qlik Account sections.
- On downloaded software such as the data gateways and mobile apps.

Review [how to apply a brand](https://qlik.dev/manage/platform-operations/brand-a-tenant)
for guidance on deployment, and for examples.

## Curate hub layouts and content

Using collections and homes, you can set a default view for your users that guides
them to only the content you wish to present.

![Direct access to the Qlik Cloud Hub, highlighting the custom home, generic link, and public collection](https://qlik.dev/_astro/brand-hub-home.CCb7wlQj.png)

Improve the onboarding experience for new users by:

- Providing links to your own content using [Generic Links](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-generic-links.htm),
  which appear as tiles
  in the hub with an image of your choice (currently available for
  creation via user interface only).
- Curating [public collections](https://community.qlik.com/t5/Design/Public-collections-A-powerful-way-to-organize-content/ba-p/2160642)
  to guide users to important content when they enter
  their tenant.
- Customize the layout when a user logs in with [custom home pages](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-customized-home.htm).

## Qlik Sense styling

Qlik Sense offers various approaches for brand control:

- [Custom themes](https://qlik.dev/extend/create-custom-themes) offer extensive styling that can
  be applied to individual Qlik Sense apps.
- [App styling](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/style-app.htm)
  via the app settings pane provides control over the general look and feel of an app, including:
  - App icon - shown in the hub and within the app
  - Open app options
  - Reading order
  - Header logo and color in sheets
  - Visibility of toolbar and header in sheets
  - Visibility of hover menu and context menus on objects
  - Visibility of items in visualization menus
- [Sheet styling](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/styling-sheets.htm)
  allows you to set per-sheet visual properties.
- [Visualization styling](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/change-appearance-of-visualization.htm)
  allows you to make fine grain changes to individual visualization objects in a sheet.
- Objects such as the [Layout container](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/layout-container.htm)
  enable creation of complex interfaces by adding multiple visualizations, layering them,
  adding conditions for when they appear, and more.

## Next steps

**Ready to continue?** → [Data modeling strategy](https://qlik.dev/manage/oem/solution-architecture/data-modeling/)
