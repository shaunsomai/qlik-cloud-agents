---
source: https://qlik.dev/manage/automate/find-orphaned-license-assignments/
last_updated: 2026-01-19T14:21:00Z
---

# Find orphaned license assignments

## List assignments not on the current tenant

Assignment of licenses is keyed on the user `subject`, which is a unique string
provided by your Identity Provider. These assignments are handled separately from users
in the tenant, since a single entitlement can support more than one Qlik Cloud tenant,
or Qlik Sense Enterprise Client-managed site.
As a result, the `users` API returns only users on that tenant, while `licenses/assignments` returns all global
assignments to that entitlement.

If you have only one tenant and want to track down assignments not linked to users,
this automation snippet returns a list of them. You can also view these users
in the [Qlik Cloud Management Console](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/SaaS-invite-users-capacity-model.htm#anchor-3)
by navigating to `Users` and selecting `Orphans` in the dropdown.

![example output showing orphaned entitlements](https://qlik.dev/_astro/license-orphans.BcPbb8Un.png)

<details>
<summary>Automation snippet</summary>

To call via an automation, and output a table of assignments, copy, and paste this
snippet into a new automation workspace:

```json
{"blocks":[{"id":"E3E724B2-A5E8-4865-88D6-3D32514B1181","type":"StartBlock","disabled":false,"name":"Start","displayName":"Start","comment":"","childId":"D0FA6C62-3093-4C9C-9659-486E2B18E9A2","inputs":[{"id":"run_mode","value":"manual","type":"select","structure":{}}],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":0},{"id":"1AB4517E-0BDB-4F65-8684-B281C99022B6","type":"EndpointBlock","disabled":false,"name":"rawAPIListRequest","displayName":"Qlik Cloud Services - Raw API List Request","comment":"","childId":"61212565-8914-4A1E-B50B-BB727D346AC7","inputs":[{"id":"c3a1c780-2076-11ec-98c4-dd329f9ef682","value":"licenses/assignments","type":"string","structure":[]},{"id":"c6915fb0-2839-11ec-a450-03c7d8aebbe7","value":[{"key":"orphans","value":"true"}],"type":"object","mode":"keyValue","structure":[]}],"settings":[{"id":"maxitemcount","value":"","type":"string","structure":[]},{"id":"blendr_on_error","value":"stop","type":"select","structure":[]},{"id":"cache","value":"0","type":"select","structure":[]},{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":640,"loopBlockId":"E278D040-E0F4-4412-A486-163B0CEBA7A0","datasourcetype_guid":"61a87510-c7a3-11ea-95da-0fb0c241e75c","endpoint_guid":"4b993580-2072-11ec-8f59-e5aaa8656a36","endpoint_role":"list"},{"id":"D0FA6C62-3093-4C9C-9659-486E2B18E9A2","type":"ShowBlock","disabled":false,"name":"output","displayName":"Output","comment":"Note on the output","childId":"6CA09EB1-352A-471B-9E6E-BE4C177B5996","inputs":[{"id":"input","value":"Current orphaned assignments for this entitlement will be output below. Assignments are made to a user subject. Only assignments for users not in this tenant will be returned.","type":"string","structure":[]}],"settings":[{"id":"display_mode","value":"add","type":"select","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":120},{"id":"6CA09EB1-352A-471B-9E6E-BE4C177B5996","type":"ShowBlock","disabled":false,"name":"output2","displayName":"Output 2","comment":"Table header","childId":"94AD4B53-D0B3-41DB-9688-EC1F83774551","inputs":[{"id":"input","value":"| Output | User subject | Assignment type | \n| ------ | ------ | ------ |","type":"string","structure":[]}],"settings":[{"id":"display_mode","value":"add","type":"select","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":240},{"id":"E1465418-0D2E-4A0B-869B-AE85C25A1B7D","type":"ShowBlock","disabled":false,"name":"output3","displayName":"Output 3","comment":"Table output per assignment","childId":"4C83C1D5-8134-41AB-AD32-081870718B1F","inputs":[{"id":"input","value":"| {$.count} | {replace: {$.rawAPIListRequest.item.subject}, '|', '&#124;'} | {$.rawAPIListRequest.item.type} |","type":"string","structure":[]}],"settings":[{"id":"display_mode","value":"add","type":"select","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":120,"y":460},{"id":"61212565-8914-4A1E-B50B-BB727D346AC7","type":"ShowBlock","disabled":false,"name":"output4","displayName":"Output 4","comment":"Output complete.","childId":"9B9D7C14-FEFB-45FA-A860-F7CD2D02DD28","inputs":[{"id":"input","value":"Output complete for { $.count } assignments.","type":"string","structure":[]}],"settings":[{"id":"display_mode","value":"add","type":"select","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":1300},{"id":"94AD4B53-D0B3-41DB-9688-EC1F83774551","type":"VariableBlock","disabled":false,"name":"count","displayName":"Variable - count","comment":"","childId":"1AB4517E-0BDB-4F65-8684-B281C99022B6","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":0,"y":360,"variableGuid":"3E60E53B-B716-4606-A095-4BB6BA3EB27F","operations":[{"id":"set_value","key":"71FD2AAB-DD64-42A6-B3BE-EC8F19BFD985","name":"Set value of { variable }","value":"0"}]},{"id":"E278D040-E0F4-4412-A486-163B0CEBA7A0","type":"VariableBlock","disabled":false,"name":"count","displayName":"Variable - count","comment":"","childId":"E1465418-0D2E-4A0B-869B-AE85C25A1B7D","inputs":[],"settings":[],"collapsed":[{"name":"loop","isCollapsed":false}],"x":120,"y":700,"variableGuid":"3E60E53B-B716-4606-A095-4BB6BA3EB27F","operations":[{"id":"add","key":"944B6106-9F1A-4D61-BA34-B69A43039C44","name":"Add to { variable }","value":"1"}]},{"id":"4C83C1D5-8134-41AB-AD32-081870718B1F","type":"UpdateJobBlock","disabled":false,"name":"updateRunTitle","displayName":"Update Run Title","comment":"","childId":null,"inputs":[{"id":"title","value":"Printing assignment { $.count }","type":"string","structure":[]}],"settings":[{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":120,"y":820},{"id":"9B9D7C14-FEFB-45FA-A860-F7CD2D02DD28","type":"UpdateJobBlock","disabled":false,"name":"updateRunTitle2","displayName":"Update Run Title 2","comment":"","childId":null,"inputs":[{"id":"title","value":"Output complete for { $.count } assignments.","type":"string","structure":[]}],"settings":[{"id":"automations_censor_data","value":false,"type":"checkbox","structure":[]}],"collapsed":[{"name":"loop","isCollapsed":false}],"x":370,"y":820}],"variables":[{"guid":"3E60E53B-B716-4606-A095-4BB6BA3EB27F","name":"count","type":"number"},{"guid":"C824FF00-2EFF-43A1-B4ED-BD6E0395C501","name":"users","type":"object"},{"guid":"1CB3311F-0745-4623-B0C2-330B36BFE372","name":"user","type":"object"}]}
```

</details>

For more information on the underlying API, see the [license
assignments endpoint description](https://qlik.dev/apis/rest/licenses/#%23%2Fentries%2Fv1%2Flicenses%2Fassignments-get).
