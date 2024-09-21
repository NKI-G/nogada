use bevy::prelude::*;
use bevy::window::PrimaryWindow;

fn main(){
    App::new()
        .add_plugins(DefaultPlugins)
        .add_systems(Startup, spawn_camera)
        .add_systems(Startup, spawn_book)
        .run();
}

#[derive(Component)]
pub struct Book{}

pub fn spawn_book(
    mut commands: Commands,
    asset_server: Res<AssetServer>,
){
    for i in 1..4 {
        for j in 1..20 {
            let mut path = String::from("Images/Book/");
            path.push_str(&i.to_string());
            path.push_str("line/pastel_rainbow_");
            path.push_str(&j.to_string());
            path.push_str(".png");

            commands.spawn((
                SpriteBundle {
                    transform: Transform {
                        translation: Vec3::new((j * 60) as f32, (i * 120) as f32, 0.0),
                        scale: Vec3::new(0.02, 0.02, 0.0),
                        ..default()
                    },
                    texture: asset_server.load(path),
                    ..default()
                },
                Book {}
            ));
        }
    }
}


pub fn spawn_camera(
    mut commands: Commands,
    window_query: Query<&Window, With<PrimaryWindow>>
){
    let window: &Window = window_query.get_single().unwrap();

    commands.spawn(
        Camera2dBundle{
            transform: Transform::from_xyz(window.width() / 2.0, window.height() / 2.0, 0.0),
            ..default()
        },
    );
}