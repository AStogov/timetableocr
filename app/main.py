from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.ocr.v20181119 import ocr_client, models
import json
from app import handle
def main(imgurl):
    try: 
        cred = credential.Credential("", "") 
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile) 

        req = models.TableOCRRequest()
        params = '{"ImageUrl":"' + imgurl + '"}'
        req.from_json_string(params)

        resp = client.TableOCR(req)
        data = handle.handle(resp.to_json_string())
        data = json.loads(data)
        return data
        
    except TencentCloudSDKException as err: 
        return err