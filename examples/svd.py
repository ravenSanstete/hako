from .context import monad
from .context import tangle
from .context import feeder 
from .context import prototype
from .context import magica
from .context import hako

from connectors import ml_100k_conn as conn

ip='10.141.246.29';
port=27017;


version='100k';
batch_size=100;
connector=conn.MLConnector(ip,port,version);

print(connector.feed_train_batch(batch_size));






#
