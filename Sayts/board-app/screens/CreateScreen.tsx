import { View, Text } from 'react-native'
import React from 'react'

interface Props {
    onCreated: () => void
}

export default function CreateScreen({onCreated}: Props) {
  return (
    <View>
      <Text>CreateScreen</Text>
    </View>
  )
}