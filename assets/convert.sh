#!/bin/bash
umlet -action=convert -format=png -filename=reports_classes.uxf
umlet -action=convert -format=png -filename=meetingmeister.usecases.uxf
umlet -action=convert -format=png -filename=meetingmeister.actions.uxf
umlet -action=convert -format=png -filename=datenmeister.web.navigation.uxf
mv *.uxf.png ../docs/images/