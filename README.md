# fe-sms-server

[![Build Status](https://travis-ci.org/fernandoe/fe-sms-server.svg?branch=feature-enviar-mensagem)](https://travis-ci.org/fernandoe/fe-sms-server)



## AWS



### Environment Variables

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY



### AWS Example Response

```json
{
  "MessageId": "402b0d22-2c59-5209-98ec-5e60661fb591",
  "ResponseMetadata": {
    "RequestId": "df5bb2dc-36b4-5641-90c0-e19e7cf261d9",
    "HTTPStatusCode": 200,
    "HTTPHeaders": {
      "x-amzn-requestid": "df5bb2dc-36b4-5641-90c0-e19e7cf261d9",
      "content-type": "text/xml",
      "content-length": "294",
      "date": "Sat, 07 Apr 2018 04:24:37 GMT"
    },
    "RetryAttempts": 0
  }
}
```



#### References

* https://stackoverflow.com/questions/38358733/how-do-i-send-an-sms-message-via-aws-sns-using-boto3-in-an-aws-lambda-function
* https://bradmontgomery.net/blog/sending-sms-messages-amazon-sns-and-python/
* https://erudinsky.com/2017/09/14/how-to-send-sms-using-amazon-sns-and-python
* http://blog.outcome.io/sending-a-text-message-with-sns/
* http://2017.compciv.org/guide/topics/aws/intro-to-aws-boto3.html
