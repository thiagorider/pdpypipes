#!/usr/bin/env python3

import os
import sys, argparse
from unicodedata import name
import pdpyras


def eventTrigger(routing_key, summary, source, component, buildstate, buildnumber, link, severity):
    """
        Trigger an incident for pipeline
    """
    try:
        session = pdpyras.EventsAPISession(routing_key)
    except:
        print("Error: Can't open session")
        sys.exit(1)
    
    try:
        session.trigger(summary, source, None, severity, {"component": component}, {"Build State": buildstate, "Build Number": buildnumber}, None, [{"href": link,"text": "Pipeline Link"}])
    except pdpyras.PDHTTPError as apierror:
        print("Error: " + apierror.msg)
        sys.exit(1)
        
    return 0

def main(argv):

    # Create the parser
    parser = argparse.ArgumentParser(description='Trigger an alert on PagerDuty API from Azure Pipelines')

    # Add the arguments
    parser.add_argument('summary',
                        metavar='summary',
                        type=str,
                        help='the summary of the event')
    parser.add_argument('source',
                        metavar='source',
                        type=str,
                        help='the source of the event')
    parser.add_argument('component',
                        metavar='component',
                        type=str,
                        help='the component of the event')
    parser.add_argument('buildstate',
                        metavar='buildstate',
                        type=str,
                        help='the build state of the pipeline')
    parser.add_argument('buildnumber',
                        metavar='buildnumber',
                        type=str,
                        help='the build number of the pipeline')
    parser.add_argument('link',
                        metavar='link',
                        type=str,
                        help='the link for the pipeline')
    parser.add_argument('severity',
                        metavar='severity',
                        type=str,
                        help='the severity of the event')

    # Execute parse_args()
    args = parser.parse_args()
    
    try:
        routing_key = os.environ['PD_API_KEY']
    except KeyError:
        print("PD_API_KEY is not defined")
        sys.exit(1)

    eventTrigger(routing_key, args.summary, args.source, args.component, args.buildstate, args.buildnumber, args.link, args.severity)


if __name__ == "__main__":
   main(sys.argv[1:])