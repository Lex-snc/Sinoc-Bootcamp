import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, ImageBackground, TouchableOpacity, useWindowDimensions, Platform } from 'react-native';
import React from 'react';

export default function App() {
  const { width, height } = useWindowDimensions();

  const handlePress = () => {
    alert('Back Off Dude!');
  };

  return (
    <ImageBackground
      source={require('./sample.jpg')}
      style={styles.container}
    >
      <View style={[styles.overlay, { padding: width * 0.05, width: width * 0.9 }]}> 
        <Text style={[styles.subtitle, { fontSize: height * 0.04, marginBottom: height * 0.03 }]}>What a Beautiful Yaaaaannnnnnnnnggggggggg uwu!</Text>

        <TouchableOpacity style={[styles.button, { paddingVertical: height * 0.02, paddingHorizontal: width * 0.1 }]} onPress={handlePress}>
          <Text style={[styles.buttonText, { fontSize: height * 0.025 }]}>Exactly!</Text>
        </TouchableOpacity>
      </View>

      <StatusBar style={Platform.OS === 'ios' ? 'light' : 'auto'} />
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    resizeMode: 'cover',
  },
  overlay: {
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    borderRadius: 10,
  },
  subtitle: {
    fontWeight: 'bold',
    color: 'white',
    textAlign: 'center',
    textShadowColor: 'black',
    textShadowOffset: { width: 1, height: 1 },
    textShadowRadius: 3,
  },
  button: {
    backgroundColor: '#ff6347',
    borderRadius: 10,
    marginTop: 20,
  },
  buttonText: {
    fontWeight: 'bold',
    color: 'white',
    textAlign: 'center',
  },
});