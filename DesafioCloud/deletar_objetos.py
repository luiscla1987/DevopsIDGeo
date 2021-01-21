import boto3
import datetime


class DelObjects(object):

    def __init__(self, bucketName, typeResource, yearLimit, mouthLimit, dayLimit):
        self._bucketName = bucketName
        self._typeResource = typeResource
        self._yearLimit = yearLimit
        self._mouthLimit = mouthLimit
        self._dayLimit = dayLimit

    def deleteObjects(self):
        s3 = boto3.resource(self._typeResource)
        bucket = s3.Bucket(self._bucketName)
        for each_object in bucket.objects.all():
            if(each_object.last_modified).replace(tzinfo=None) <= datetime.datetime(self._yearLimit, self._mouthLimit, self._dayLimit, tzinfo=None):
                each_object.delete()


if __name__ == '__main__':
    # Passar como parâmetro (BucketName, TypeResource, YEAR = YYYY, Mouth = MM, Day = DD) * Data Limite
    deletarObjetos = DelObjects("awscode", "s3", 2019, 12, 1)
    deletarObjetos.deleteObjects()
