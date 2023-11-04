---
title: repl.email
---
Repl.email was great while it lasted, but sadly is no longer in service.

# [repl.email](https://repl.email) - a fully fledged, free email service for replit users

![repl.email](static/images/repl.email/demo.gif)

[*check out the repl.email noticeboard here!*](https://notes.marcusj.org/link/repl.email)

---

I [started work on repl.email](https://notes.marcusj.org/link/blog#replemail) late 2020. My goal was to host my own email service - like gmail. However, in order to host this on [replit](https://repl.email/__repl), I had to think outside the box. Replit only allows you to open a single port for hosting a webserver, so I found two third-party services that I would use to make this work.

## [SendGrid](https://sendgrid.com/)

By taking advantage of their free API, I can link my account to the domain I own, and send emails out to anyone, anywhere. They also support additional features such as scheduled delivery up to `72 hours` in advance, which I incorporated into [repl.email](https://repl.email).

## [ImprovMX](https://improvmx.com/)

Yet another free service, improvmx lets me forward all emails sent to my domain (`repl.email`) to a set of mailboxes. For the mailbox I used gmail, and sorted emails into individual inboxes.

# Features

* live markdown editor
* save emails as drafts to continue editing later
* schedule email delivery up to 72 hours
* feature-wide api access
* login via QR code or replit
* attatch files
* flag emails as important/unread + pin emails
* read receipts