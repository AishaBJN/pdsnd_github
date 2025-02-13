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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input(' Please choose city ( chicago , new york city , washington) ' ).lower() 
    if city not in ['chicago' , 'new york city' , 'washington']: 
        city = input(' please choose between( chicago, new york city , washington) ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input(' Please choose month ' ).lower() 
    if month not in ['all','january', 'february', 'march', 'april', 'may', 'june']: 
         month = input(' please choose between( january, february, march, april, may, june or all ) ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(' Please choose day ').lower()
    if day not in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all']: 
         day = input(' please choose between( Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all) ').lower()

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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
     
    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1
        
       df = df[df['month'] == month]

    if day != 'all':
       df = df[df['day_of_week'] == day.title()]
  
    return df

    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print('the most common month: ', popular_month)

    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]

    print('the most common day of week: ', popular_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('most commonly used start station:', Start_Station)

    # TO DO: display most commonly used end station
    end_Station = df['End Station'].value_counts().idxmax()
    print('most commonly used end station:', end_Station)

    # TO DO: display most frequent combination of start station and end station trip
    
    combination = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending = False).head(1) 
    print('most frequent combination of start station and end station trip:\n', combination)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('total travel time is: ', total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('mean travel time is: ', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types\n' , user_types) 

    # TO DO: Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print('counts of gender\n ' , gender)
        
    else:
        print(" Gender Types: No data available for this month. ")


    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest_y = df['Birth Year'].min()
        recent_m = df['month'].max()
        recent_y = df['Birth Year'].max()
        common_y = df['Birth Year'].mode()[0]
        print(' Earliest year of birth is {} and Most recent year of birth is {} and most common year of birth {} and Most recent month of birth is {} '.format(earliest_y , recent_y , common_y, recent_m )) 
        
    else:
        print(" Gender Types: No data available for this month. ")

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? ").lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(" Nice Work ")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
