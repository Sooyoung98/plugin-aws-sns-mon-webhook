import logging
import unittest
import os
import json
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.tester import TestCase, print_json
from pprint import pprint

_LOGGER = logging.getLogger(__name__)


class TestEvent(TestCase):
    def test_parse(self):
        param = {"options": {},
                 "data": {
                     "MessageId": "3f78eee9-6691-51be-b77e-b4603c34d486", "Timestamp": "2022-02-18T08:27:17.407Z",
                     "TopicArn": "arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev", "SignatureVersion": "1",
                     "Type": "Notification",
                     "SigningCertURL": "https://sns.ap-southeast-2.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",
                     "UnsubscribeURL": "https://sns.ap-southeast-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev:46b11fb0-b7d8-4ae9-934c-2593a89a79fb",
                     "Message": "{\n  \"version\": \"0\",\n  \"id\": \"7bf73129-1428-4cd3-a780-95db273d1602\",\n  \"detail-type\": \"AWS Health Event\",\n  \"source\": \"aws.health\",\n  \"account\": \"123456789012\",\n  \"time\": \"2016-06-05T06:27:57Z\",\n  \"region\": \"ap-southeast-2\",\n  \"resources\": [],\n  \"detail\": {\n    \"eventArn\": \"arn:aws:health:ap-southeast-2::event/AWS_ELASTICLOADBALANCING_API_ISSUE_90353408594353980\",\n    \"service\": \"ELASTICLOADBALANCING\",\n    \"eventTypeCode\": \"AWS_ELASTICLOADBALANCING_API_ISSUE\",\n    \"eventTypeCategory\": \"issue\",\n    \"startTime\": \"Sat, 04 Jun 2016 05:01:10 GMT\",\n    \"endTime\": \"Sat, 04 Jun 2016 05:30:57 GMT\",\n    \"eventDescription\": [{\n      \"language\": \"en_US\",\n      \"latestDescription\": \"A description of the event will be provided here\"\n    }]\n  }\n}",
                     "Signature": "X/CKfxDEiAOUmx9exJHB0ChOMwxOy+pzvb37OP3NA9c1ttVy5CDRkHa8lTLnos3h7CYSzdKFaUMWp/xhIbdXeRzM/HzaVUH+GseJrZFZDi1dvMSjtbacmSNO2Sxkjc6yaqht9zyh3C/8BEN1uQuCQh5bGriV2Ty4/LrxvrX/y4qF2JWmXnQacsaOWYqQWUBLcoPS19fD5X+Cs9OunQW1ZdWGPVumTC8gx3Pdx1Zf7Htd7sz5JXmiryMVCyP8iBWAdpjycVIZJV2+OcjQ5Vv+L52zkiU9Y3EUYgCmx8mkOR6SGjfasL0KfQ890mMR7+MsOqRgMFKakesFq9COzgp55Q=="}
                 }
        param1 = {"options": {},
                  "data": {
                      "Signature": "O965M1pBN5oCvh5DRyvoYjV8eaZjUwS/o0CR7/ddCwYfpDXkprAELHyDHp5KDy1Hs+6ZP19BWXPhejPzgJKkkfz6R4/oVyDEVF+NTKLNl9Khq2EDSlpP6LhYMpu5rjyOMseu5OB/5YJN0EFlo/a8I1QBZBaRcpG3swfDTRg2/hLRy92JIFkO0WHlK0iVCMntMnsEg5WDQ+kzXqUIqKIihI81y+0sS15eiXiUJ38IDdPeEVDeQrvuZHfc2yAxqRC0L1c206ZqOOdf8gkW3MXcoFfwiPgZQgFQxwJ/9z065ZGvSSlmuQ/R17z2VmQTouL6b7l7LjaZ9fPFksIdAca5sw==",
                      "SignatureVersion": "1",
                      "Message": "{\n  \"version\": \"0\",\n  \"id\": \"7bf73129-1428-4cd3-a780-95db273d1602\",\n  \"detail-type\": \"AWS Health Event\",\n  \"source\": \"aws.health\",\n  \"account\": \"123456789012\",\n  \"time\": \"2016-06-05T06:27:57Z\",\n  \"region\": \"us-west-2\",\n  \"resources\": [\"i-abcd1111\"],\n  \"detail\": {\n    \"eventArn\": \"arn:aws:health:us-west-2::event/AWS_EC2_INSTANCE_STORE_DRIVE_PERFORMANCE_DEGRADED_90353408594353980\",\n    \"service\": \"EC2\",\n    \"eventTypeCode\": \"AWS_EC2_INSTANCE_STORE_DRIVE_PERFORMANCE_DEGRADED\",\n    \"eventTypeCategory\": \"issue\",\n    \"startTime\": \"Sat, 05 Jun 2016 15:10:09 GMT\",\n    \"eventDescription\": [{\n      \"language\": \"en_US\",\n      \"latestDescription\": \"A description of the event will be provided here\"\n    }],\n    \"affectedEntities\": [{\n      \"entityValue\": \"i-abcd1111\",\n      \"tags\": {\n        \"stage\": \"prod\",\n        \"app\": \"my-app\"\n      }\n    }]\n  }\n}",
                      "SigningCertURL": "https://sns.ap-southeast-2.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",
                      "Timestamp": "2022-02-18T08:32:39.194Z", "Type": "Notification",
                      "UnsubscribeURL": "https://sns.ap-southeast-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev:46b11fb0-b7d8-4ae9-934c-2593a89a79fb",
                      "TopicArn": "arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev",
                      "MessageId": "8c9bce44-3a81-544d-bd36-94cd6166fb31"}
                  }
        param2 = {"options": {},
                  "data": {
                      "UnsubscribeURL": "https://sns.ap-southeast-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev:46b11fb0-b7d8-4ae9-934c-2593a89a79fb",
                      "MessageId": "5f348269-339e-5e41-88e6-d8e06fc1989f", "SignatureVersion": "1",
                      "Type": "Notification",
                      "Signature": "oar3KkfeJFzrmFmchcYjH6Sqx0TjgUs/YZ/9FIR8YopYMqCDSX8eZQYmfJQXR8gkuc8ZnCvqAEJ72XFHkIZERTrr2sDeZJ/e85ukZoIaAIsLkuEM4QvyZJOcLTTmqoFC1/NWj/QdJTExBvx9E0Opr+YA4BV5TTUdqXo4JJY5aYYlE25JQmmOCRUAVeTYFkTAmBE0kd03flRkpPR4Gib21pnlTYD4bfAttr2k+hPq8r8w1s8wJnu5u0ua6qKdyTvfQMX6Fx/eSk8OgPDTFZRslvMDQixGS/aLF1D5im7nwMlRkPQn4jAKGyXPLrs5KB5Mn89NGUwDCPt41LENfvFoiQ==",
                      "Message": "{\n  \"version\": \"0\",\n  \"id\": \"7bf73129-1428-4cd3-a780-95db273d1602\",\n  \"detail-type\": \"AWS Health Abuse Event\",\n  \"source\": \"aws.health\",\n  \"account\": \"123456789012\",\n  \"time\": \"2018-08-01T06:27:57Z\",\n  \"region\": \"global\",\n  \"resources\": [\"arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111\", \"arn:aws:ec2:us-east-1:123456789012:instance/i-abcd2222\"],\n  \"detail\": {\n    \"eventArn\": \"arn:aws:health:global::event/AWS_ABUSE_DOS_REPORT_92387492375_4498_2018_08_01_02_33_00\",\n    \"service\": \"ABUSE\",\n    \"eventTypeCode\": \"AWS_ABUSE_DOS_REPORT\",\n    \"eventTypeCategory\": \"issue\",\n    \"startTime\": \"Wed, 01 Aug 2018 06:27:57 GMT\",\n    \"eventDescription\": [{\n      \"language\": \"en_US\",\n      \"latestDescription\": \"A description of the event will be provided here\"\n    }],\n    \"affectedEntities\": [{\n      \"entityValue\": \"arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111\"\n    }, {\n      \"entityValue\": \"arn:aws:ec2:us-east-1:123456789012:instance/i-abcd2222\"\n    }]\n  }\n}",
                      "SigningCertURL": "https://sns.ap-southeast-2.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",
                      "Timestamp": "2022-02-18T08:34:39.768Z",
                      "TopicArn": "arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev"}
                  }
        param3 = {"options": {},
                  "data": {
                      "SigningCertURL": "https://sns.ap-southeast-2.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",
                      "TopicArn": "arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev",
                      "Timestamp": "2022-02-18T08:35:33.452Z",
                      "Type": "Notification", "SignatureVersion": "1",
                      "Signature": "D1dd2IK8X+QUAZahFKkv0Ka8MKK7T3hPs9GKD6ANikv9UDV+cPGINMcfBB6EzL76aK4HnhL8vUTz/8bV46Xhh0EIVp0uepssk9ef7lh3dl69c3G63WtJM8WmLuWiQqvAILctKy9WLUl5twPQJJ+4n0wBFafWIvKGvwoA29E+QrwTsSOBk/7ZyfHRdeBBK/jNjwOBT1iJL9SIsT6+iOANr7SzhJ0Sk/SqjoQSZsb1TJvLXKu6I6D9Vv1yI/yfXdvtr4Ff6guBL6I+DE+6luQfxigzsUdsCjUlAbiLNmvsG44k6uMKfU22CwocBbLsuQkuYt73Kks4CaVE/vl+GsHc2g==",
                      "MessageId": "3737b6d6-1c86-59a2-9111-ec5f4013dd65",
                      "Message": "{\n  \"version\": \"0\",\n  \"id\": \"7bf73129-1428-4cd3-a780-95db273d1602\",\n  \"detail-type\": \"AWS Health Abuse Event\",\n  \"source\": \"aws.health\",\n  \"account\": \"123456789012\",\n  \"time\": \"2018-08-02T05:30:00Z\",\n  \"region\": \"global\",\n  \"resources\": [\"arn:aws:cloudfront::123456789012:distribution/DSF867DUMMY87SDF\", \"arn:aws:ec2:us-east-1:123456789012:instance/i-abcd2222\"],\n  \"detail\": {\n    \"eventArn\": \"arn:aws:health:global::event/AWS_ABUSE_COPYRIGHT_DMCA_REPORT_2345235545_5323_2018_08_02_02_12_98\",\n    \"service\": \"ABUSE\",\n    \"eventTypeCode\": \"AWS_ABUSE_COPYRIGHT_DMCA_REPORT\",\n    \"eventTypeCategory\": \"issue\",\n    \"startTime\": \"Thu, 02 Aug 2018 05:30:00 GMT\",\n    \"eventDescription\": [{\n      \"language\": \"en_US\",\n      \"latestDescription\": \"A description of the event will be provided here\"\n    }],\n    \"affectedEntities\": [{\n      \"entityValue\": \"arn:aws:cloudfront::123456789012:distribution/DSF867DUMMY87SDF\"\n    }, {\n      \"entityValue\": \"arn:aws:ec2:us-east-1:123456789012:instance/i-abcd2222\"\n    }]\n  }\n}",
                      "UnsubscribeURL": "https://sns.ap-southeast-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-southeast-2:257706363616:phd-info-dev:46b11fb0-b7d8-4ae9-934c-2593a89a79fb"}
                  }

        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param.get('data')})
        print_json(parsed_data)
        print()
        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param1.get('data')})
        print_json(parsed_data)
        print()
        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param2.get('data')})
        print_json(parsed_data)
        print()
        parsed_data = self.monitoring.Event.parse({'options': {}, 'data': param3.get('data')})
        print_json(parsed_data)
        print()


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
