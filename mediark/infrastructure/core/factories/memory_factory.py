from pathlib import Path
from .factory import Factory
from ..configuration import Config
from ....application.repositories import (
    ImageRepository, MemoryImageRepository,
    AudioRepository, MemoryAudioRepository)
from ....application.services import (
    AuthService, StandardAuthService,
    IdService, StandardIdService,
    FileStoreService, MemoryFileStoreService,
    ImageFileStoreService, MemoryImageFileStoreService,
    AudioFileStoreService, MemoryAudioFileStoreService)
from ....application.coordinators import (
    ImageStorageCoordinator, AudioStorageCoordinator, SessionCoordinator)
from ....application.reporters import MediarkReporter, StandardMediarkReporter
from ....application.utilities import (
    ExpressionParser, TenantProvider, StandardTenantProvider)


class MemoryFactory(Factory):
    def __init__(self, config: Config) -> None:
        self.config = config

    # Repositories
    ##############

    def expression_parser(self) -> ExpressionParser:
        return ExpressionParser()

    def memory_image_repository(self, expression_parser: ExpressionParser
                                ) -> MemoryImageRepository:
        return MemoryImageRepository(expression_parser)

    def memory_audio_repository(self, expression_parser: ExpressionParser
                                ) -> MemoryAudioRepository:
        return MemoryAudioRepository(expression_parser)
    
    def standard_tenant_provider(self) -> StandardTenantProvider:
        return StandardTenantProvider()

    # Services
    ##########

    def standard_id_service(self) -> StandardIdService:
        return StandardIdService()
    
    def memory_auth_service(self) -> StandardAuthService:
        return StandardAuthService()

    def memory_image_file_store_service(self) -> MemoryImageFileStoreService:
        return MemoryImageFileStoreService()

    def memory_audio_file_store_service(self) -> MemoryAudioFileStoreService:
        return MemoryAudioFileStoreService()

    # Coordinators
    ##############

    def image_storage_coordinator(self, image_repository: ImageRepository,
                                  id_service: IdService,
                                  file_store_service: ImageFileStoreService
                                  ) -> ImageStorageCoordinator:
        return ImageStorageCoordinator(image_repository, id_service,
                                       file_store_service)

    def audio_storage_coordinator(self, audio_repository: AudioRepository,
                                  id_service: IdService,
                                  file_store_service: AudioFileStoreService
                                  ) -> AudioStorageCoordinator:
        return AudioStorageCoordinator(audio_repository, id_service,
                                       file_store_service)
    
    def session_coordinator(
        self, tenant_provider: TenantProvider, auth_service: AuthService
    ) -> SessionCoordinator:
        return SessionCoordinator(tenant_provider, auth_service)

    # Reporters
    ##############

    def memory_mediark_reporter(self, image_repository: ImageRepository,
                                audio_repository: AudioRepository
                                ) -> StandardMediarkReporter:
        return StandardMediarkReporter(image_repository, audio_repository)