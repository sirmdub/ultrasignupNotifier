# ultrasignupNotifier
to watch ultrasignup for race registration opening


### Todo

- [ ] Store/Retrieve/Replace urls in Redis
- [ ] Docker Build
- [ ] Deploy Script

### Race Registration Check Workflow
* Get race http page
* If "Registration closes"
  * Send notification, Registration is Open
* If "This Event Took Place"
  * Get link to "See the 20xx event"
  * Update URL that is checked to latest
  * Restart function
