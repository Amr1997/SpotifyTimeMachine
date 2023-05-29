# Spotify Time Machine

Welcome to Spotify Time Machine, a Python script that creates a playlist of your favorite songs from a specific time period in the past. This project uses the Spotify Web API to access your Spotify account and create a new playlist.

## Installation

To get started, clone this repository to your local machine using the following command:

```
git clone https://github.com/Amr1997/SpotifyTimeMachine.git
```

Next, navigate to the project directory and create a virtual environment:

```
cd SpotifyTimeMachine
python3 -m venv env
```

Activate the virtual environment:

```
source env/bin/activate
```

Install the project dependencies:

```
pip install -r requirements.txt
```

## Configuration

Before running the script, you need to set up a Spotify application and obtain a client ID and client secret. Follow these steps to create a Spotify application:

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in with your Spotify account.
2. Click on "Create an App" and fill in the required information.
3. Once you've created your app, click on "Edit Settings" and add `http://localhost:8000/callback/` to the "Redirect URIs" field.
4. Note down your client ID and client secret, which you'll need to configure the script.

Next, create a file called `.env` in the project directory and add the followinginformation:

```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8000/callback/
```

Replace `your_client_id` and `your_client_secret` with your actual client ID and client secret.

## Usage

To run the script, activate the virtual environment and run the following command:

```
python time_machine.py
```

The script will prompt you to enter a year and a range of months for which you want to create a playlist. It will then access your Spotify account, search for the top tracks of that time period, and create a new playlist with those tracks.

## Contributing

Contributions are welcome and appreciated! If you have any bug reports, feature requests, or questions, please open an issue on the project's GitHub page.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
