import os
from pathlib import Path
from pytest import fixture
from mediark.infrastructure.data import SwiftFileStoreService
from mediark.infrastructure.core.configuration import JsonConfig
from mediark.application.utilities import StandardTenantProvider, Tenant


@fixture
def swift_file_store_service(tmp_path):
    config = JsonConfig()['data']
    config['dir_path'] = tmp_path / 'data'
    standard_tenant_provider = StandardTenantProvider()
    standard_tenant_provider.setup(Tenant(id='2', name="custom-tenant"))
    return SwiftFileStoreService(
        standard_tenant_provider, config,
        'images', 'png')
