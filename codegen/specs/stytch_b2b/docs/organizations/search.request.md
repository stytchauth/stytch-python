Search for Organizations. If you send a request with no body params, no filtering will be applied and the endpoint will return all Organizations.

All fuzzy search filters require a minimum of at least 3 characters

Parameters:

- `cursor`: The cursor field allows you to paginate through your results. Each result array is limited to 1000 results, if your query returns more than 1000 results, you will need to paginate the responses using the cursor. If you receive a response that includes a non-null next_cursor in the results_metadata object, you should repeat the call, being sure to include all of the original fields, but pass in the next_cursor in the cursor field. Continue to make calls until the next_cursor in the response is null.

- `limit`: The number of Organizations to return per page, the default is 100. A maximum of 1000 Organizations can be returned by a single request. If the total size of your result is greater than one page size, you must paginate the response. See the cursor field below.

- `query`: The optional query object contains the operator, e.g. AND or OR, and the operands that will filter your Organizations. Only an operator is required, if you include no operands, no filtering will be applied. Similarly if you include no query object, no filtering is applied and we'll return all of your Organizations with no filtering applied.
