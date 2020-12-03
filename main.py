from pre_processing import  *
from dotenv import load_dotenv

#loading ENV variables
load_dotenv()

model_net_10_link =  os.getenv("ModelNet10Link")
sampled_data_link =  os.getenv('SampledData')


if __name__ == '__main__':
    print(model_net_10_link)
    print(sampled_data_link)