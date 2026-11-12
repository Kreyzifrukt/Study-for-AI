import { View, Text } from 'react-native'
import React from 'react'

interface Props {
  onLogout: () => void;
}

export default function ProfileScreen({ onLogout }: Props) {
  return (
    <View>
      <Text>ProfileScreen</Text>
    </View>
  )
}