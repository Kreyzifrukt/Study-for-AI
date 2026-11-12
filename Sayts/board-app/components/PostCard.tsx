import { Text, View, StyleSheet,Pressable } from 'react-native';
import React from 'react';
import { Announcement } from '../types/Announcement';

interface PostCardProps{
  announcement: Announcement,
  isOwner?: boolean;
  onEdit?: () => void;
  onDelete?: () => void;
}

export default function PostCard({
    announcement, isOwner, onEdit, onDelete
}: PostCardProps){
    return (
      <View style={styles.card}>
        <View style={styles.header}>
          <Text style={styles.title}>
            {announcement.title}
          </Text>
          <Text style={styles.title}>
            {announcement.price.toLocaleString()} грн
          </Text>
        </View>
          <Text style={styles.category}>
            {announcement.category}
          </Text>
          <View style={styles.info}>
              <Text>{announcement.city}</Text>
              <Text>{announcement.phone}</Text>
          </View>
          <Text style={styles.author}>
            {announcement.authorName}
          </Text>
          {isOwner && (
              <View style={styles.actions}>
                  <Pressable style={styles.editButton} onPress={onEdit}>
                      <Text style={styles.buttonText}>Редагувати</Text>
                  </Pressable>
                  <Pressable style={styles.deleteButton} onPress={onDelete}>
                      <Text style={styles.buttonText}>Видалити</Text>
                  </Pressable>
              </View>
          )}
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