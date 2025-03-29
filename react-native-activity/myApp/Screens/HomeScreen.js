import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

const HomeScreen = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Home Screen</Text>
      
      <Button 
        title="Go to Details" 
        onPress={() => navigation.navigate('Details')} 
      />

      <View style={styles.space} />

      <Button 
        title="Green" 
        onPress={() => navigation.navigate('Green')} 
        color="green"
      />

<Button 
        title="Pink" 
        onPress={() => navigation.navigate('Pink')} 
        color="pink"
      />

<Button 
        title="Red" 
        onPress={() => navigation.navigate('Red')} 
        color="red"
      />
    </View>
      
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f8f9fa',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  space: {
    height: 20, // Adds space between buttons
  },
});

export default HomeScreen;
