# ultrasignupNotifier
to watch ultrasignup for race registration opening


### Todo

* Notify pulled into its own def?
  * SNS figure out how to do http notification to Hipchat

### Race Registration Check Workflow
* Get race http page
* If "Registration closes"
  * Send notification, Registration is Open
* If "This Event Took Place"
  * Get link to "See the 20xx event"
  * Test link for redirects, follow them to the end
  * Update URL that is checked to latest
  * Restart function
