'''importing of s3fs for file reading'''
import s3fs

'''Importing json for conversion to json files'''

import json


class EasyS3FS():
    '''Class utilises s3fs and json libraries to grab data from Amazon s3 buckets'''
    def __init__(self,access_key,secret_key,bucket_name=''):
        '''bucket_name is the name of the s3fs bucket you want it to look inThe access key is your access key for the bucket While the secret key is the secret key for the bucket'''
        if bucket_name is None:
            #when using the printBucket because no bucket is chosen, then default
            #will be all of the buckets printed
            self.file_system= s3fs.S3FileSystem(key=access_key, secret=secret_key)
        else:

            self.file_system= s3fs.S3FileSystem(key=access_key, secret=secret_key)
            self.bucket_name = bucket_name

    def setBucketName(self,bucket_name):
        '''If you havent set a bucket name in the initialization statement (If you only put in the access key and secret key) Example: test=EasyS3FS(key,secret)'''
        # Sets the bucket_name for the bucket
        self.bucket_name = bucket_name

    def printBucket(self):
        '''This will print either the bucket name youve set, or just a list of the buckets'''
        print(self.bucket_names)


    def fileList(self):
        '''Returns a list representation of the files in the bucket'''
        return self.file_system.ls((self.bucket_name))


    def printFilesInBucket(self):
        '''Prints the Bucket names in the S3 instance'''
        if self.bucket_name is '':
            raise ValueError("Please use method 'setBucketName' to set a bucket name first ")
        else:
            for file in self.fileList():
                print(file)
    def rawFile(self,file_name):
        '''Allows someone to work with raw file imported from aws bucket'''
        if self.bucket_name is '':
            raise ValueError("Please use method 'setBucketName' to set a bucket name first ")
        else:
            file_path =self.bucket_name + '/'+ file_name
            f=self.file_system.open(file_path, 'rb')
            #returns the raw file
            return f

    def fileToJson(self,file_name):
        '''opens specified file in the bucket, decodes it into utf-8 and turns it into JSON string'''
        #checks if a bucket name has been defined
        if self.bucket_name is '':
            raise ValueError("Please use method 'setBucketName' to set a bucket name first ")
        else:
            file_path =self.bucket_name + '/'+ file_name
            f=self.file_system.open(file_path, 'rb')   #this reads the file into bytes,
            #which are turned into a Json formatted string(in utf-8) on the next line
            data=f.read().decode("utf-8")
            #returns a JSON formatted python string
            return data
    def fileToDict(self,file_name):
        '''opens specified file in the bucket, decodes it into utf-8 and turns it into JSON string this time it goes one step further and turns it into a python dictionary object this can be inerated over'''
        #checks to make sure that a bucket name has been defined
        if self.bucket_name is '':
            raise ValueError("Please use method 'setBucketName' to set a bucket name first ")
        else:
            file_path =self.bucket_name + '/'+ file_name
            f=self.file_system.open(file_path, 'rb')   #this reads the file into bytes,
            #which are turned into a Json formatted string(in utf-8) on the next line
            data=f.read().decode("utf-8")
            #turn into a python dict object
            json_dict = json.loads(data)
            #returns formatted ditcionay version
            return json_dict

    def writeToFile(self,json_dict,file_name):
        '''Takes the json_dict from the fileToDict function and writies into its json format into another part of the SystemError'''
        '''Note that file name must is also include the location. For right now this must be in json dict format, will add others later'''
        F = open(file_name ,"w")
        F.write(json_dict)
        F.close()
        print('Data written to: {}'.format(file_name))
        
    def printTest():
        print('Test')
if __name__ == '__main__':
    printTest()
