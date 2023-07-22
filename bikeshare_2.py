import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('enter city name :').lower()
    while city not in CITY_DATA :
        print('invald city')
        city = input('enter city name :').lower()
        print("the city is", city)


        # get user input for month (all, january, february, ... , june)
    months = [ "january", "february", "march", "april", "may", "june", "all"]
    month = input("Enter the month : ").lower()
    while month not in months :
        print('invalid month')
        month = input('enter month name :').lower()
        print("the month is", month)
        # get user input for day of week (all, monday, tuesday, ... sunday)
    week_days = ["saturday", "sunday" , "monday" , "tuesday" , "wednesday" , "thursday" ,"friday" ,"all"]
    day = input("enter the day please :").lower()
    while day not in week_days :
        print('invalid day')
        day = input("enter the day please :").lower()
        print("the day is",day)

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    most_common_month = df['month'].mode()[0]
    print('Most Common Month:', most_common_month)

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common day:', most_common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_station = df["Start Station"].mode()[0]
    print("the popular station is : ", popular_station)

    # display most commonly used end station
    popular_destination = df["End Station"].mode()[0]
    print("the popular destination is : ", popular_destination)

    # display most frequent combination of start station and end station trip
    df["route"] = df["Start Station"] + "-" + df["End Station"]

    popular_route = df["route"].mode()[0]

    print("the popular start to end trip is : ", popular_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = sum(df["Trip Duration"])
    print("Total travel time : ", total_travel)
    # display mean travel time
    average_travel_time = df["Trip Duration"].mean()
    print("the average time :", average_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df['User Type'].value_counts()
    print('\nUser types:\n',user_count  )
    try:

        # Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('\nBike riders gender split: \n', gender_count)

        # Display earliest, most recent, and most common year of birth
        earliest_yob = int(df['Birth Year'].min())
        most_recent_yob = int(df['Birth Year'].max())
        most_common_yob = int(df['Birth Year'].mode()[0])
        print('\n Earliest birth year :  ',earliest_yob)
        print('\n Most recent birth year :  ',most_recent_yob)
        print('\n Most common birth year :  ',most_common_yob)
        # dealing with Washington
    except KeyError:
        print('This data is not available for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_data(city):
    """The fuction takes the name of the city produced by the get_filters fuction as input and returns the raw data of that city as chunks of 5 rows based upon user input.
    """
    df = pd.read_csv(CITY_DATA[city])

    print('\nRaw data is available to check... \n')
    start_loc = 0
    while True:
        display_opt = input('To View the availbale raw data in chuncks of 5 rows type: Yes \n').lower()
        if display_opt not in ['yes', 'no']:
            print('That\'s invalid choice, pleas type yes or no')

        elif display_opt == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc+=5

        elif display_opt == 'no':
            print('\nExiting...')
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(city, month, day)
        df = load_data(city, month, day)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()