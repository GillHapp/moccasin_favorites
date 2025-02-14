from src import favorites
def deploy():
    print('Deploying favorite...')
    deploy_favorite = favorites.deploy()
    current_number = deploy_favorite.retrieve()
    print(f'Current favorite number is: {current_number}')


def moccasin_main():
    deploy()
