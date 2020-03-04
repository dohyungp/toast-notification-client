""" This module is wrapper class for Toast SMS/MMS API.
If you want use it, just use like below code.

>>> from toast_sms_client import ToastSMS
>>> tos = ToastSMS("<API-KEY>")
>>> dictionary = {
    "foo": "bar",
    ...
}
>>> tos.send_message(dictionary)
"""

from requests import Session
from jsonschema import Draft7Validator
from .schema import (
    REQUEST_SCHEMA,
    TAG_SCHEMA,
    UPLOAD_SCHEMA,
    QUERY_SCHEMA,
    CATEGORY_SCHEMA,
    TEMPLATE_SCHEMA
)


class ToastSMS:
    """NHN TOAST SMS(MMS) Wrapper
    """
    def __init__(self, app_key, version='v2.2'):
        """Toast SMS initialze with app key and version.

        :param app_key: Toast API App Key
        :param version: Toast API version Default `v2.2`.
        :returns: None.
        """
        base = 'https://api-sms.cloud.toast.com'
        self.domain = '/'.join([base, 'sms', version, 'appKeys', app_key])
        self.basic_validator = Draft7Validator(REQUEST_SCHEMA)
        self.tag_validator = Draft7Validator(TAG_SCHEMA)
        self.upload_validator = Draft7Validator(UPLOAD_SCHEMA)
        self.query_validator = Draft7Validator(QUERY_SCHEMA)
        self.category_validator = Draft7Validator(CATEGORY_SCHEMA)
        self.template_validator = Draft7Validator(TEMPLATE_SCHEMA)
        self.session = Session()

    def call(self, end_point, method='get', params=None, json=None):
        """Call API Method via Requests Session.
        :param end_point: end_point represented like `/sender/mms`.
        :param method: http methods(GET, POST, PUT, DELETE, HEAD etc)
        :param params: url paramters.
        :param json: json object.
        :returns: session Requests object.
        """
        if end_point[0] == '/':
            url = self.domain + end_point
        else:
            url = self.domain + '/' + end_point

        headers = {'Content-Type': 'application/json;charset=UTF-8'}

        return self.session.request(method,
                                    url,
                                    headers=headers,
                                    params=params,
                                    json=json)

    def add_category(self, json):
        """Add Category to Toast Cloud SMS
        :param json: json object.
        :returns: post result.
        """
        self.category_validator.validate(json)
        res = self.call('/categories', 'post', json=json)
        res.raise_for_status()
        return res.json()

    def inquiry_category(self, params=None, category_id=None):
        """Inquiry Category to Toast Cloud SMS
        :param params: url parameter.
        :param category_id: category id.
        :returns: queried result.
        """
        if category_id:
            res = self.call('/categories/{0}'.format(category_id))
        else:
            res = self.call('/categories', params=params)
        res.raise_for_status()
        return res.json()

    def update_category(self, category_id, json):
        """Update Category to Toast Cloud SMS
        :param category_id: will update category_id
        :param json: json object.
        :returns: put result.
        """
        self.category_validator.validate(json)
        end_point = '/categories/{0}'.format(category_id)
        res = self.call(end_point, 'put', json=json)
        res.raise_for_status()
        return res.json()

    def delete_category(self, category_id):
        """Delete Category from Toast Cloud SMS
        :param category_id: will delete category_id
        :param json: json object.
        :returns: delete result.
        """
        res = self.call('/categories/{0}'.format(category_id), 'delete')
        res.raise_for_status()
        return res.json()

    def add_template(self, json, category_id=0):
        """Add Template to Toast Cloud SMS.
        :param json: json object.
        :param category_id: Only need for not passed category id via json.
        :returns: post result.
        """
        if 'categoryId' not in json:
            json['categoryId'] = category_id

        self.template_validator.validate(json)
        res = self.call('/templates', 'post', json=json)
        res.raise_for_status()
        return res.json()

    def inquiry_template(self, params=None, template_id=None):
        """Inquiry template to Toast Cloud SMS
        :param params: url parameter(categoryId, useYn, pageSize, pageNum, totalCount)
        :returns: queried result.
        """
        if template_id:
            res = self.call('/templates/{0}'.format(template_id))
        else:
            res = self.call('/templates', params=params)
        res.raise_for_status()
        return res.json()

    def update_template(self, template_id, json):
        """Update Template to Toast Cloud SMS
        :param template_id: will update template_id
        :param json: json object.
        :returns: put result.
        """
        self.template_validator.validate(json)
        end_point = '/templates/{0}'.format(template_id)
        res = self.call(end_point, 'put', json=json)
        res.raise_for_status()
        return res.json()

    def delete_template(self, template_id):
        """Delete Category from Toast Cloud SMS
        :param template_id: will delete template_id
        :param json: json object.
        :returns: delete result.
        """
        res = self.call('/templates/{0}'.format(template_id), 'delete')
        res.raise_for_status()
        return res.json()

    def send_message(self, json):
        """Send Message via API(MMS, SMS)
        :param json: json object.
        :returns: post result.
        """
        self.basic_validator.validate(json)
        send_type = json.pop('sendType')
        end_point = '/sender/{0}'.format(send_type)
        res = self.call(end_point, 'post', json=json)
        res.raise_for_status()
        return res.json()

    def inquiry_sent_result(self, params):
        """Inquiry sent Message Result from API(MMS, SMS)
        :param json: json object.
        :returns: json object about queried set.
        """
        self.query_validator.validate(params)
        send_type = params.pop('sendType')
        end_point = '/sender/{0}'.format(send_type)
        res = self.call(end_point, params=params)
        res.raise_for_status()
        return res.json()

    def send_tag_message(self, json):
        """Send Tag Message to API(MMS, SMS)
        :param json: json object.
        :returns: post result.
        """
        self.tag_validator.validate(json)
        send_type = json.pop('sendType')
        end_point = '/tag-sender/{0}'.format(send_type)
        res = self.call(end_point, 'post', json=json)
        res.raise_for_status()
        return res.json()

