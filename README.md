<p align="center">
  <img src="http://i.imgur.com/uYtVENE.png" alt="Slacker">
</p>

# zappa-slack-inviter

A teeny tiny server-less Slack channel inviter.

## Installation

```
git clone https://github.com/Miserlou/zappa-slack-inviter
cd zappa-slack-inviter
virtualenv env; source env/bin/active; pip install -r requirements.txt
```

Then add your [token](https://api.slack.com/docs/oauth-test-tokens) into `app.py` using your favorite text editor, then `zappa init` and `zappa deploy`.

## Custom Domains

To deploy your inviter with a custom domain and auto-renewing Let's Encrypt certificate, see [this chapter of the Zappa documentation](https://github.com/Miserlou/Zappa/blob/master/docs/domain_with_free_ssl_dns.md).
