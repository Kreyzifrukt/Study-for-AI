import { View, Text, StyleSheet } from 'react-native'
import React, { Component } from 'react'

interface Props {
  screen: string;
  setScreen: (screen: string) => void;
}

export default function BottomNav({ screen, setScreen}: Props) {
  return (
    <View>
      <Text>BottomNav</Text>
    </View>
  )
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: "#fff",
    borderRadius: 12,
    padding: 16,
    marginBottom: 14,
    shadowColor: "#000",
    shadowOpacity: 0.08,
    shadowRadius: 6,
    shadowOffset: {
      width: 0,
      height: 2,
    },
    elevation: 3,
  },

  header: {
    flexDirection: "row",
    justifyContent: "space-between",
    gap: 10,
  },

  title: {
    flex: 1,
    fontSize: 19,
    fontWeight: "700",
  },

  price: {
    fontSize: 18,
    fontWeight: "700",
  },

  category: {
    marginTop: 6,
    fontSize: 13,
    color: "#666",
  },

  description: {
    marginTop: 12,
    fontSize: 15,
    lineHeight: 22,
  },

  info: {
    marginTop: 14,
    gap: 5,
  },

  author: {
    marginTop: 12,
    color: "#666",
  },

  actions: {
    flexDirection: "row",
    gap: 10,
    marginTop: 15,
  },

  editButton: {
    backgroundColor: "#1976d2",
    padding: 10,
    borderRadius: 8,
  },

  deleteButton: {
    backgroundColor: "#d32f2f",
    padding: 10,
    borderRadius: 8,
  },

  buttonText: {
    color: "#fff",
    fontWeight: "600",
  },
});