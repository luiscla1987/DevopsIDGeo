import boto3


class Instancia(object):

    def __init__(self, profileName, serviceName, regionName, instances):
        self._profileName = profileName
        self._serviceName = serviceName
        self._regionName = regionName
        self._instances = instances

    def connection(self):
        aws_mag_con_root = boto3.session.Session(
            profile_name=self._profileName)
        self._ec2_con_cli = aws_mag_con_root.client(
            service_name=self._serviceName, region_name=self._regionName)
        return self._ec2_con_cli.describe_instances()['Reservations']

    def hasInstance(self):
        response = self.connection()
        for each_item in response:
            try:
                for each_instance in each_item['Instances']:
                    if((each_instance['InstanceId'] in self._instances) and (each_instance['State']['Name'] == "stopped")):
                        self._ec2_con_cli.start_instances(
                            InstanceIds=[each_instance['InstanceId']])
                        print("Starting...")
            except:
                print("Error Unexpected")


if __name__ == '__main__':
    # Passar como parâmetro (ProfileName, ServiceName, RegionName, Instances)
    instancia = Instancia("root", "ec2", "us-east-2",
                          ["i-011f8a89551fad09c"])
    instancia.hasInstance()
