---
source: https://qlik.dev/extend/extensions/extension-api/build-extension/get-additional-data/
last_updated: 2026-06-02T18:15:45+01:00
---

# Retrieve additional data

The number of rows and columns retrieved with the first paint call is normally
defined in `initialProperties`. But there are instances when this is not enough.

The maximum number of cells (`qWidth * qHeight`) allowed in an initial data fetch
is 10,000. Retrieve additional data in chunks using the `getData` method in the
Backend API.

## Examples

```javascript
var requestPage = [{
    qTop : lastrow + 1,
    qLeft : 0,
    qWidth : 10, //should be # of columns
    qHeight : Math.min(50, this.backendApi.getRowCount() - lastrow)
}];
$element.find("#more").on("click", function() {
    self.backendApi.getData(requestPage).then(function(dataPages) {
        self.paint($element);
    });
});
```

> **Note:** The call is asynchronous and returns a promise.
> You need to trigger the actual re-paint after the call has completed and you do this using the `then()` method.

Example: Retrieving additional data in chunks

In this example, the `getData` method will get the cells defined
by `requestPage` and return the cells in the `dataPages` parameter. It will
also update the layout buffer used by `eachDataRow` so when the paint function is
called again, it will have all rows. This usage means the visualization will
build up gradually.

```javascript
paint: function ( $element ) {
     var lastrow = 0, me = this;
     //loop through the rows we have and render
     this.backendApi.eachDataRow( function ( rownum, row ) {
                lastrow = rownum;
                //do something with the row..
     });
     if(this.backendApi.getRowCount() > lastrow +1){
             //we haven't got all the rows yet, so get some more, 1000 rows
              var requestPage = [{
                    qTop: lastrow + 1,
                    qLeft: 0,
                    qWidth: 10, //should be # of columns
                    qHeight: Math.min( 1000, this.backendApi.getRowCount() - lastrow )
                }];
               this.backendApi.getData( requestPage ).then( function ( dataPages ) {
                        //when we get the result trigger paint again
                        me.paint( $element );
               } );
     }
 
}
```
