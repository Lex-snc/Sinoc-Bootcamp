import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

const HomeScreen = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>GREEN</Text>
      
      <Button 
        title="Go to Home" 
        onPress={() => navigation.navigate('Home')} 
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

      
<Button 
        title="Green" 
        onPress={() => navigation.navigate('Green')} 
        color="green"
      />

    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'green',
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
