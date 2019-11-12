# import numpy as np
# from matplotlib.pylab import ylim, title, ylabel, xlabel
# import matplotlib.pyplot as plt
from kalman_filter import SingleStateKalmanFilter
# from moving_average import MovingAverageFilter

# Create some random temperature data
def kalman_filter_rssi(self,devrssi):
    # devrssi= np.random.normal(-65, 5, size=(1, 100)).flatten()
    devrssi=self.devrssi
    random_data_init=devrssi

    # Initialise the Kalman Filter

    A = 1  # No process innovation
    C = 1  # Measurement
    B = 0  # No control input
    Q = 0.005  # Process covariance
    R = 3  # Measurement covariance
    x = -56  # Initial estimate
    P = 5  # Initial covariance

    kalman_filter = SingleStateKalmanFilter(A, B, C, x, P, Q, R)

    # Initialise two moving average filters with different window lengths
    # ma5_filter = MovingAverageFilter(5)
    # ma50_filter = MovingAverageFilter(50)

    # Empty lists for capturing filter estimates
    kalman_filter_estimates = []
    # ma5_filter_estimates = []
    # ma50_filter_estimates = []

    # Simulate the data arriving sequentially
    for data in random_data_init:
        # ma5_filter.step(data)
        # ma5_filter_estimates.append(ma5_filter.current_state())

        # ma50_filter.step(data)
        # ma50_filter_estimates.append(ma50_filter.current_state())

        kalman_filter.step(0, data)
        X=kalman_filter.current_state()
    return(X)


# Plot the Data for Presentation
# plt.plot(random_data_init, 'r*')
# title("Filtering Real-Time Data")
# ylabel('RSSI dBm')
# xlabel('Sample')
# ylim([-15,-85])
# plt.plot(ma5_filter_estimates, 'b', linewidth=2.0)
# plt.plot(ma50_filter_estimates, 'g', linewidth=2.0)
# plt.plot(kalman_filter_estimates, 'k', linewidth=2.0)
#
# Show the plot
# plt.show()
