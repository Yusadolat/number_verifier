from dateutil import parser
import requests


class VerifiedOwner:
    status = False
    response = ''

    def __init__(self, response):
        self.response = response
        response_status = response.get('status')
        if str(response_status) != "404":
            self.status = True

    def get_owner(self):
        if self.status:
            return self.response.get('owner')
        return "Unknown"

    def get_model(self):
        if self.status:
            return self.response.get('model')
        return "Unknown"

    def get_colour(self):
        if self.status:
            return self.response.get('color')
        return "Unknown"

    def get_chasis_number(self):
        if self.status:
            return self.response.get('chasis')
        return "Unknown"

    def get_issue_date(self):
        if self.status:
            return parser.parse(self.response.get('licenseIssueDate'))
        return "Unknown"

    def get_expiry_date(self):
        if self.status:
            return parser.parse(self.response.get('licenseExpiryDate'))
        return "Unknown"


class VerifyOwner:
    number = ''

    def __init__(self, number):
        self.number = number

    def verify(self):
        try:
            response = requests.get("https://mvrd.herokuapp.com/api/plates/%s" % self.number)
            return VerifiedOwner(response=response.json())
        except Exception:
            return VerifiedOwner(response={u'status': 404, u'message': u"Plate number details not available"})
