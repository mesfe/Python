#preparing data
import numpy as np
import pandas as pd

listing=pd.read_csv("finaldata/listings_all.csv", encoding = "ISO-8859-1",low_memory=False)


#converting price datatype to int. Some of the prices is saved with dollar signs and commas
if listing['price'].dtype!='int64' and listing['price'][0]=="$":
    listing['price']=listing['price'].map(lambda p: int(p[1:-3].replace(",", "")))

#In this step we want to know about presence or absence of amenities a home offers. To do that we create a dictionary of
#all amenities offered by all homes then compare each home with this list and give True and False values


#clean the amenities column. Amenities column is saved as a set so we need to get the members of this set in a list

listing['amenities'] = listing['amenities'].apply( lambda amns: "|".join([amn.replace("}", "").replace("{", "").replace('"', "") for amn in amns.split("|")]) if isinstance(amns, str) else amns)


#get a list of unique amenities
amenities = np.unique(np.concatenate(listing['amenities'].apply(lambda amns: amns.split(",") if isinstance(amns, str) else []).values ))

#check if a listing has a specific amenities from the amenities dictionary.
amenities_matrix = np.array([listing['amenities'].apply(lambda amns: amn in amns   ).values for amn in amenities])


#pick some of the columns from df dataframe and creat a new dataframe
features=listing[['host_listings_count', 'host_total_listings_count', 'accommodates',
                     'bathrooms', 'bedrooms', 'beds', 'price', 'guests_included', 'number_of_reviews',
                     'review_scores_rating']]

#add amnities_matrix which cotains data about presence and absence of amenities for each listing to features dataframe
features=pd.concat([features, pd.DataFrame(data=amenities_matrix.T, columns=amenities)], axis=1)


#some of the columns in features dataframe are saved as strings of the form "t" or "f". Map them to boolean values

for boolean_feature in ['host_is_superhost', 'host_identity_verified', 'host_has_profile_pic',
                   'is_location_exact', 'requires_license', 'instant_bookable',
                   'require_guest_profile_picture', 'require_guest_phone_verification']:
    features[boolean_feature] = listing[boolean_feature].map(lambda s: False if s == "f" else True)


#Encode city column to dummy variables using get_dummies function and add it to feautures dataframe

features = pd.concat([features, pd.get_dummies(listing['city']).astype(np.bool)], axis=1)



#fill null values with the median of the columns

for col in features.columns[features.isnull().any()]:
    features[col] = features[col].fillna(features[col].median())


#writing to csv
features.to_csv('finaldata/listings_all_clean.csv')


