# hello, orquestra

Source: http://docs.orquestra.io/tutorials/hello-workflow/

## Running

``` sh
qe login -s <URL>
qe submit workflow welcome-worlkflow.yaml
qe get workflow hello-workflow-<UID>
qe get workflowresult hello-workflow-<UID>

```

Results:

``` json
{
  "hello-workflow-<UID>": {
    "workflowId": "hello-workflow-<UID>",
    "welcome": {
      "schema": "message",
      "message": "Welcome to Orquestra!"
    },
    "stepName": "greeting",
    "stepID": "hello-workflow-<UID>"
  }
```

## Notes

- The result above is is different from [the tutorial snippet](http://docs.orquestra.io/tutorials/hello-workflow/#downloading-the-results).:

- I can see only a single step despite the caption telling otherwise.
    - "Note that this workflow has another step after the first greeting step. That step is added in the next tutorial, Hello Component"
    
- It'd be cool to create another function in tutorial page 2, not the exact copy of the one used on page 1.

- Is there any way to make feedback loop shorter?

- What's the purpose of specifying "types"? Seems like it doesn't provide any new information to the system.

- Broken link in http://docs.orquestra.io/tutorials/ml-basic-3/#6-combining-code-from-different-components
