#!/bin/bash

umlet -action=convert -format=png -filename=reports_classes.uxf
umlet -action=convert -format=png -filename=meetingmeister.usecases.uxf
umlet -action=convert -format=png -filename=meetingmeister.actions.uxf

mv reports_classes.uxf.png ../docs/images/

