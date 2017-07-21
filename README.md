# ultrasignupNotifier
to watch ultrasignup for race registration opening


### Todo

* tests/comingsoon.htm needs tests in test.py
* getNextEventURL returns "i got nothing", which could fail silently. FIX!
* Need to check if anything other than 200? Does this fail silently for example, 40x, 50x?
* Cloudwatch alarm setup with deploy?
* Trim out any size/cruft in the zip build process to have as lightweight as possible
* Notify pulled into its own def?
  * SNS figure out how to do http notification to Hipchat
  * Post notification events to db?
* API Gateway App to monitor / manage the data

### Race Registration Check Workflow
* Get race http page
* If "Registration closes"
  * Send notification, Registration is Open
* If "This Event Took Place"
  * Get link to "See the 20xx event"
  * Test link for redirects, follow them to the end
  * Update URL that is checked to latest
  * Restart function
