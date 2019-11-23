from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.ocr.v20181119 import ocr_client, models
import json
import handle
try: 
    cred = credential.Credential("AKIDUq170gMH8l9IH3Cty3vZzB9uQgrnlw9f", "UjiT1OXZMvEH6g166MN8evzpPpBIAm9I") 
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile) 

    req = models.TableOCRRequest()
    params = '{"ImageUrl":"http://oken.club/capture.png"}'
    req.from_json_string(params)

    resp = client.TableOCR(req)
    data = handle.handle(resp.to_json_string())
    data = json.loads(data)
    print(data)
    
except TencentCloudSDKException as err: 
    print(err)