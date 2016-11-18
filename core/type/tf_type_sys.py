import tensorflow as tf

# variable
variable=tf.Variable;


# constant
constant=tf.constant;


# random variable, which is higher-ordered
gaussian_rv=tf.random_normal;
uniform_rv=tf.random_uniform;
multinomial_rv=tf.multinomial;
gamma_rv=tf.random_gamma;

# data alignment types, only of the common usage
float16=tf.float16;
float32=tf.float32;
float64=tf.float64;

uint16=tf.uint16;

int16=tf.int16;
int32=tf.int32;
int64=tf.int64;

bool=tf.bool;
string=tf.string;






def srand(seed):
    tf.set_random_seed(seed);
