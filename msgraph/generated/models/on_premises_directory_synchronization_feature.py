from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class OnPremisesDirectorySynchronizationFeature(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def block_cloud_object_takeover_through_hard_match_enabled(self,) -> Optional[bool]:
        """
        Gets the blockCloudObjectTakeoverThroughHardMatchEnabled property value. The blockCloudObjectTakeoverThroughHardMatchEnabled property
        Returns: Optional[bool]
        """
        return self._block_cloud_object_takeover_through_hard_match_enabled
    
    @block_cloud_object_takeover_through_hard_match_enabled.setter
    def block_cloud_object_takeover_through_hard_match_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockCloudObjectTakeoverThroughHardMatchEnabled property value. The blockCloudObjectTakeoverThroughHardMatchEnabled property
        Args:
            value: Value to set for the blockCloudObjectTakeoverThroughHardMatchEnabled property.
        """
        self._block_cloud_object_takeover_through_hard_match_enabled = value
    
    @property
    def block_soft_match_enabled(self,) -> Optional[bool]:
        """
        Gets the blockSoftMatchEnabled property value. The blockSoftMatchEnabled property
        Returns: Optional[bool]
        """
        return self._block_soft_match_enabled
    
    @block_soft_match_enabled.setter
    def block_soft_match_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockSoftMatchEnabled property value. The blockSoftMatchEnabled property
        Args:
            value: Value to set for the blockSoftMatchEnabled property.
        """
        self._block_soft_match_enabled = value
    
    @property
    def bypass_dir_sync_overrides_enabled(self,) -> Optional[bool]:
        """
        Gets the bypassDirSyncOverridesEnabled property value. The bypassDirSyncOverridesEnabled property
        Returns: Optional[bool]
        """
        return self._bypass_dir_sync_overrides_enabled
    
    @bypass_dir_sync_overrides_enabled.setter
    def bypass_dir_sync_overrides_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the bypassDirSyncOverridesEnabled property value. The bypassDirSyncOverridesEnabled property
        Args:
            value: Value to set for the bypassDirSyncOverridesEnabled property.
        """
        self._bypass_dir_sync_overrides_enabled = value
    
    @property
    def cloud_password_policy_for_password_synced_users_enabled(self,) -> Optional[bool]:
        """
        Gets the cloudPasswordPolicyForPasswordSyncedUsersEnabled property value. The cloudPasswordPolicyForPasswordSyncedUsersEnabled property
        Returns: Optional[bool]
        """
        return self._cloud_password_policy_for_password_synced_users_enabled
    
    @cloud_password_policy_for_password_synced_users_enabled.setter
    def cloud_password_policy_for_password_synced_users_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the cloudPasswordPolicyForPasswordSyncedUsersEnabled property value. The cloudPasswordPolicyForPasswordSyncedUsersEnabled property
        Args:
            value: Value to set for the cloudPasswordPolicyForPasswordSyncedUsersEnabled property.
        """
        self._cloud_password_policy_for_password_synced_users_enabled = value
    
    @property
    def concurrent_credential_update_enabled(self,) -> Optional[bool]:
        """
        Gets the concurrentCredentialUpdateEnabled property value. The concurrentCredentialUpdateEnabled property
        Returns: Optional[bool]
        """
        return self._concurrent_credential_update_enabled
    
    @concurrent_credential_update_enabled.setter
    def concurrent_credential_update_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the concurrentCredentialUpdateEnabled property value. The concurrentCredentialUpdateEnabled property
        Args:
            value: Value to set for the concurrentCredentialUpdateEnabled property.
        """
        self._concurrent_credential_update_enabled = value
    
    @property
    def concurrent_org_id_provisioning_enabled(self,) -> Optional[bool]:
        """
        Gets the concurrentOrgIdProvisioningEnabled property value. The concurrentOrgIdProvisioningEnabled property
        Returns: Optional[bool]
        """
        return self._concurrent_org_id_provisioning_enabled
    
    @concurrent_org_id_provisioning_enabled.setter
    def concurrent_org_id_provisioning_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the concurrentOrgIdProvisioningEnabled property value. The concurrentOrgIdProvisioningEnabled property
        Args:
            value: Value to set for the concurrentOrgIdProvisioningEnabled property.
        """
        self._concurrent_org_id_provisioning_enabled = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new onPremisesDirectorySynchronizationFeature and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The blockCloudObjectTakeoverThroughHardMatchEnabled property
        self._block_cloud_object_takeover_through_hard_match_enabled: Optional[bool] = None
        # The blockSoftMatchEnabled property
        self._block_soft_match_enabled: Optional[bool] = None
        # The bypassDirSyncOverridesEnabled property
        self._bypass_dir_sync_overrides_enabled: Optional[bool] = None
        # The cloudPasswordPolicyForPasswordSyncedUsersEnabled property
        self._cloud_password_policy_for_password_synced_users_enabled: Optional[bool] = None
        # The concurrentCredentialUpdateEnabled property
        self._concurrent_credential_update_enabled: Optional[bool] = None
        # The concurrentOrgIdProvisioningEnabled property
        self._concurrent_org_id_provisioning_enabled: Optional[bool] = None
        # The deviceWritebackEnabled property
        self._device_writeback_enabled: Optional[bool] = None
        # The directoryExtensionsEnabled property
        self._directory_extensions_enabled: Optional[bool] = None
        # The fopeConflictResolutionEnabled property
        self._fope_conflict_resolution_enabled: Optional[bool] = None
        # The groupWriteBackEnabled property
        self._group_write_back_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The passwordSyncEnabled property
        self._password_sync_enabled: Optional[bool] = None
        # The passwordWritebackEnabled property
        self._password_writeback_enabled: Optional[bool] = None
        # The quarantineUponProxyAddressesConflictEnabled property
        self._quarantine_upon_proxy_addresses_conflict_enabled: Optional[bool] = None
        # The quarantineUponUpnConflictEnabled property
        self._quarantine_upon_upn_conflict_enabled: Optional[bool] = None
        # The softMatchOnUpnEnabled property
        self._soft_match_on_upn_enabled: Optional[bool] = None
        # The synchronizeUpnForManagedUsersEnabled property
        self._synchronize_upn_for_managed_users_enabled: Optional[bool] = None
        # The unifiedGroupWritebackEnabled property
        self._unified_group_writeback_enabled: Optional[bool] = None
        # The userForcePasswordChangeOnLogonEnabled property
        self._user_force_password_change_on_logon_enabled: Optional[bool] = None
        # The userWritebackEnabled property
        self._user_writeback_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesDirectorySynchronizationFeature:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesDirectorySynchronizationFeature
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesDirectorySynchronizationFeature()
    
    @property
    def device_writeback_enabled(self,) -> Optional[bool]:
        """
        Gets the deviceWritebackEnabled property value. The deviceWritebackEnabled property
        Returns: Optional[bool]
        """
        return self._device_writeback_enabled
    
    @device_writeback_enabled.setter
    def device_writeback_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceWritebackEnabled property value. The deviceWritebackEnabled property
        Args:
            value: Value to set for the deviceWritebackEnabled property.
        """
        self._device_writeback_enabled = value
    
    @property
    def directory_extensions_enabled(self,) -> Optional[bool]:
        """
        Gets the directoryExtensionsEnabled property value. The directoryExtensionsEnabled property
        Returns: Optional[bool]
        """
        return self._directory_extensions_enabled
    
    @directory_extensions_enabled.setter
    def directory_extensions_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the directoryExtensionsEnabled property value. The directoryExtensionsEnabled property
        Args:
            value: Value to set for the directoryExtensionsEnabled property.
        """
        self._directory_extensions_enabled = value
    
    @property
    def fope_conflict_resolution_enabled(self,) -> Optional[bool]:
        """
        Gets the fopeConflictResolutionEnabled property value. The fopeConflictResolutionEnabled property
        Returns: Optional[bool]
        """
        return self._fope_conflict_resolution_enabled
    
    @fope_conflict_resolution_enabled.setter
    def fope_conflict_resolution_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the fopeConflictResolutionEnabled property value. The fopeConflictResolutionEnabled property
        Args:
            value: Value to set for the fopeConflictResolutionEnabled property.
        """
        self._fope_conflict_resolution_enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "block_cloud_object_takeover_through_hard_match_enabled": lambda n : setattr(self, 'block_cloud_object_takeover_through_hard_match_enabled', n.get_bool_value()),
            "block_soft_match_enabled": lambda n : setattr(self, 'block_soft_match_enabled', n.get_bool_value()),
            "bypass_dir_sync_overrides_enabled": lambda n : setattr(self, 'bypass_dir_sync_overrides_enabled', n.get_bool_value()),
            "cloud_password_policy_for_password_synced_users_enabled": lambda n : setattr(self, 'cloud_password_policy_for_password_synced_users_enabled', n.get_bool_value()),
            "concurrent_credential_update_enabled": lambda n : setattr(self, 'concurrent_credential_update_enabled', n.get_bool_value()),
            "concurrent_org_id_provisioning_enabled": lambda n : setattr(self, 'concurrent_org_id_provisioning_enabled', n.get_bool_value()),
            "device_writeback_enabled": lambda n : setattr(self, 'device_writeback_enabled', n.get_bool_value()),
            "directory_extensions_enabled": lambda n : setattr(self, 'directory_extensions_enabled', n.get_bool_value()),
            "fope_conflict_resolution_enabled": lambda n : setattr(self, 'fope_conflict_resolution_enabled', n.get_bool_value()),
            "group_write_back_enabled": lambda n : setattr(self, 'group_write_back_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "password_sync_enabled": lambda n : setattr(self, 'password_sync_enabled', n.get_bool_value()),
            "password_writeback_enabled": lambda n : setattr(self, 'password_writeback_enabled', n.get_bool_value()),
            "quarantine_upon_proxy_addresses_conflict_enabled": lambda n : setattr(self, 'quarantine_upon_proxy_addresses_conflict_enabled', n.get_bool_value()),
            "quarantine_upon_upn_conflict_enabled": lambda n : setattr(self, 'quarantine_upon_upn_conflict_enabled', n.get_bool_value()),
            "soft_match_on_upn_enabled": lambda n : setattr(self, 'soft_match_on_upn_enabled', n.get_bool_value()),
            "synchronize_upn_for_managed_users_enabled": lambda n : setattr(self, 'synchronize_upn_for_managed_users_enabled', n.get_bool_value()),
            "unified_group_writeback_enabled": lambda n : setattr(self, 'unified_group_writeback_enabled', n.get_bool_value()),
            "user_force_password_change_on_logon_enabled": lambda n : setattr(self, 'user_force_password_change_on_logon_enabled', n.get_bool_value()),
            "user_writeback_enabled": lambda n : setattr(self, 'user_writeback_enabled', n.get_bool_value()),
        }
        return fields
    
    @property
    def group_write_back_enabled(self,) -> Optional[bool]:
        """
        Gets the groupWriteBackEnabled property value. The groupWriteBackEnabled property
        Returns: Optional[bool]
        """
        return self._group_write_back_enabled
    
    @group_write_back_enabled.setter
    def group_write_back_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the groupWriteBackEnabled property value. The groupWriteBackEnabled property
        Args:
            value: Value to set for the groupWriteBackEnabled property.
        """
        self._group_write_back_enabled = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def password_sync_enabled(self,) -> Optional[bool]:
        """
        Gets the passwordSyncEnabled property value. The passwordSyncEnabled property
        Returns: Optional[bool]
        """
        return self._password_sync_enabled
    
    @password_sync_enabled.setter
    def password_sync_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordSyncEnabled property value. The passwordSyncEnabled property
        Args:
            value: Value to set for the passwordSyncEnabled property.
        """
        self._password_sync_enabled = value
    
    @property
    def password_writeback_enabled(self,) -> Optional[bool]:
        """
        Gets the passwordWritebackEnabled property value. The passwordWritebackEnabled property
        Returns: Optional[bool]
        """
        return self._password_writeback_enabled
    
    @password_writeback_enabled.setter
    def password_writeback_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordWritebackEnabled property value. The passwordWritebackEnabled property
        Args:
            value: Value to set for the passwordWritebackEnabled property.
        """
        self._password_writeback_enabled = value
    
    @property
    def quarantine_upon_proxy_addresses_conflict_enabled(self,) -> Optional[bool]:
        """
        Gets the quarantineUponProxyAddressesConflictEnabled property value. The quarantineUponProxyAddressesConflictEnabled property
        Returns: Optional[bool]
        """
        return self._quarantine_upon_proxy_addresses_conflict_enabled
    
    @quarantine_upon_proxy_addresses_conflict_enabled.setter
    def quarantine_upon_proxy_addresses_conflict_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the quarantineUponProxyAddressesConflictEnabled property value. The quarantineUponProxyAddressesConflictEnabled property
        Args:
            value: Value to set for the quarantineUponProxyAddressesConflictEnabled property.
        """
        self._quarantine_upon_proxy_addresses_conflict_enabled = value
    
    @property
    def quarantine_upon_upn_conflict_enabled(self,) -> Optional[bool]:
        """
        Gets the quarantineUponUpnConflictEnabled property value. The quarantineUponUpnConflictEnabled property
        Returns: Optional[bool]
        """
        return self._quarantine_upon_upn_conflict_enabled
    
    @quarantine_upon_upn_conflict_enabled.setter
    def quarantine_upon_upn_conflict_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the quarantineUponUpnConflictEnabled property value. The quarantineUponUpnConflictEnabled property
        Args:
            value: Value to set for the quarantineUponUpnConflictEnabled property.
        """
        self._quarantine_upon_upn_conflict_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("blockCloudObjectTakeoverThroughHardMatchEnabled", self.block_cloud_object_takeover_through_hard_match_enabled)
        writer.write_bool_value("blockSoftMatchEnabled", self.block_soft_match_enabled)
        writer.write_bool_value("bypassDirSyncOverridesEnabled", self.bypass_dir_sync_overrides_enabled)
        writer.write_bool_value("cloudPasswordPolicyForPasswordSyncedUsersEnabled", self.cloud_password_policy_for_password_synced_users_enabled)
        writer.write_bool_value("concurrentCredentialUpdateEnabled", self.concurrent_credential_update_enabled)
        writer.write_bool_value("concurrentOrgIdProvisioningEnabled", self.concurrent_org_id_provisioning_enabled)
        writer.write_bool_value("deviceWritebackEnabled", self.device_writeback_enabled)
        writer.write_bool_value("directoryExtensionsEnabled", self.directory_extensions_enabled)
        writer.write_bool_value("fopeConflictResolutionEnabled", self.fope_conflict_resolution_enabled)
        writer.write_bool_value("groupWriteBackEnabled", self.group_write_back_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("passwordSyncEnabled", self.password_sync_enabled)
        writer.write_bool_value("passwordWritebackEnabled", self.password_writeback_enabled)
        writer.write_bool_value("quarantineUponProxyAddressesConflictEnabled", self.quarantine_upon_proxy_addresses_conflict_enabled)
        writer.write_bool_value("quarantineUponUpnConflictEnabled", self.quarantine_upon_upn_conflict_enabled)
        writer.write_bool_value("softMatchOnUpnEnabled", self.soft_match_on_upn_enabled)
        writer.write_bool_value("synchronizeUpnForManagedUsersEnabled", self.synchronize_upn_for_managed_users_enabled)
        writer.write_bool_value("unifiedGroupWritebackEnabled", self.unified_group_writeback_enabled)
        writer.write_bool_value("userForcePasswordChangeOnLogonEnabled", self.user_force_password_change_on_logon_enabled)
        writer.write_bool_value("userWritebackEnabled", self.user_writeback_enabled)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def soft_match_on_upn_enabled(self,) -> Optional[bool]:
        """
        Gets the softMatchOnUpnEnabled property value. The softMatchOnUpnEnabled property
        Returns: Optional[bool]
        """
        return self._soft_match_on_upn_enabled
    
    @soft_match_on_upn_enabled.setter
    def soft_match_on_upn_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the softMatchOnUpnEnabled property value. The softMatchOnUpnEnabled property
        Args:
            value: Value to set for the softMatchOnUpnEnabled property.
        """
        self._soft_match_on_upn_enabled = value
    
    @property
    def synchronize_upn_for_managed_users_enabled(self,) -> Optional[bool]:
        """
        Gets the synchronizeUpnForManagedUsersEnabled property value. The synchronizeUpnForManagedUsersEnabled property
        Returns: Optional[bool]
        """
        return self._synchronize_upn_for_managed_users_enabled
    
    @synchronize_upn_for_managed_users_enabled.setter
    def synchronize_upn_for_managed_users_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the synchronizeUpnForManagedUsersEnabled property value. The synchronizeUpnForManagedUsersEnabled property
        Args:
            value: Value to set for the synchronizeUpnForManagedUsersEnabled property.
        """
        self._synchronize_upn_for_managed_users_enabled = value
    
    @property
    def unified_group_writeback_enabled(self,) -> Optional[bool]:
        """
        Gets the unifiedGroupWritebackEnabled property value. The unifiedGroupWritebackEnabled property
        Returns: Optional[bool]
        """
        return self._unified_group_writeback_enabled
    
    @unified_group_writeback_enabled.setter
    def unified_group_writeback_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the unifiedGroupWritebackEnabled property value. The unifiedGroupWritebackEnabled property
        Args:
            value: Value to set for the unifiedGroupWritebackEnabled property.
        """
        self._unified_group_writeback_enabled = value
    
    @property
    def user_force_password_change_on_logon_enabled(self,) -> Optional[bool]:
        """
        Gets the userForcePasswordChangeOnLogonEnabled property value. The userForcePasswordChangeOnLogonEnabled property
        Returns: Optional[bool]
        """
        return self._user_force_password_change_on_logon_enabled
    
    @user_force_password_change_on_logon_enabled.setter
    def user_force_password_change_on_logon_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the userForcePasswordChangeOnLogonEnabled property value. The userForcePasswordChangeOnLogonEnabled property
        Args:
            value: Value to set for the userForcePasswordChangeOnLogonEnabled property.
        """
        self._user_force_password_change_on_logon_enabled = value
    
    @property
    def user_writeback_enabled(self,) -> Optional[bool]:
        """
        Gets the userWritebackEnabled property value. The userWritebackEnabled property
        Returns: Optional[bool]
        """
        return self._user_writeback_enabled
    
    @user_writeback_enabled.setter
    def user_writeback_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the userWritebackEnabled property value. The userWritebackEnabled property
        Args:
            value: Value to set for the userWritebackEnabled property.
        """
        self._user_writeback_enabled = value
    

