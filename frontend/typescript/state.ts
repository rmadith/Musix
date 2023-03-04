export interface User {
  id: string;
  name: string;
  email: string;
  // true if user is currently hosting a session
  streaming: boolean;
  activeSessions: {
    id: string;
    creatorName: string;
    creatorId: string;
    theme: string
  }[];
  topArtists: {
    name: string;
    image: string;
  }[];
  topTracks: {
    name: string;
    image: string;
    artist: string;
  }[];
}

export interface Session {
  id: string;
  theme: {
    id: string;
    name: string;
  }
  creatorName: string;
  participants: string[];
  createdAt: Date;
}