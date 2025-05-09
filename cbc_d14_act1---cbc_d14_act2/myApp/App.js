import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from './Screens/HomeScreen';
import DetailsScreen from './Screens/DetailsScreen';
import GreenScreen from './Screens/GreenScreen';
import PinkScreen from './Screens/PinkScreen';
import RedScreen from './Screens/RedScreen';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Details" component={DetailsScreen} />
        <Stack.Screen name="Green" component={GreenScreen} />
        <Stack.Screen name="Red" component={RedScreen} />
        <Stack.Screen name="Pink" component={PinkScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
