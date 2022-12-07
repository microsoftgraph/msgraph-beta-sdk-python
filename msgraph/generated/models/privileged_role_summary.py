from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
role_summary_status = lazy_import('msgraph.generated.models.role_summary_status')

class PrivilegedRoleSummary(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new privilegedRoleSummary and sets the default values.
        """
        super().__init__()
        # The number of users that have the role assigned and the role is activated.
        self._elevated_count: Optional[int] = None
        # The number of users that have the role assigned but the role is deactivated.
        self._managed_count: Optional[int] = None
        # true if the role activation requires MFA. false if the role activation doesn't require MFA.
        self._mfa_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Possible values are: ok, bad. The value depends on the ratio of (managedCount / usersCount). If the ratio is less than a predefined threshold, ok is returned. Otherwise, bad is returned.
        self._status: Optional[role_summary_status.RoleSummaryStatus] = None
        # The number of users that are assigned with the role.
        self._users_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedRoleSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedRoleSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedRoleSummary()
    
    @property
    def elevated_count(self,) -> Optional[int]:
        """
        Gets the elevatedCount property value. The number of users that have the role assigned and the role is activated.
        Returns: Optional[int]
        """
        return self._elevated_count
    
    @elevated_count.setter
    def elevated_count(self,value: Optional[int] = None) -> None:
        """
        Sets the elevatedCount property value. The number of users that have the role assigned and the role is activated.
        Args:
            value: Value to set for the elevatedCount property.
        """
        self._elevated_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "elevated_count": lambda n : setattr(self, 'elevated_count', n.get_int_value()),
            "managed_count": lambda n : setattr(self, 'managed_count', n.get_int_value()),
            "mfa_enabled": lambda n : setattr(self, 'mfa_enabled', n.get_bool_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(role_summary_status.RoleSummaryStatus)),
            "users_count": lambda n : setattr(self, 'users_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def managed_count(self,) -> Optional[int]:
        """
        Gets the managedCount property value. The number of users that have the role assigned but the role is deactivated.
        Returns: Optional[int]
        """
        return self._managed_count
    
    @managed_count.setter
    def managed_count(self,value: Optional[int] = None) -> None:
        """
        Sets the managedCount property value. The number of users that have the role assigned but the role is deactivated.
        Args:
            value: Value to set for the managedCount property.
        """
        self._managed_count = value
    
    @property
    def mfa_enabled(self,) -> Optional[bool]:
        """
        Gets the mfaEnabled property value. true if the role activation requires MFA. false if the role activation doesn't require MFA.
        Returns: Optional[bool]
        """
        return self._mfa_enabled
    
    @mfa_enabled.setter
    def mfa_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the mfaEnabled property value. true if the role activation requires MFA. false if the role activation doesn't require MFA.
        Args:
            value: Value to set for the mfaEnabled property.
        """
        self._mfa_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("elevatedCount", self.elevated_count)
        writer.write_int_value("managedCount", self.managed_count)
        writer.write_bool_value("mfaEnabled", self.mfa_enabled)
        writer.write_enum_value("status", self.status)
        writer.write_int_value("usersCount", self.users_count)
    
    @property
    def status(self,) -> Optional[role_summary_status.RoleSummaryStatus]:
        """
        Gets the status property value. Possible values are: ok, bad. The value depends on the ratio of (managedCount / usersCount). If the ratio is less than a predefined threshold, ok is returned. Otherwise, bad is returned.
        Returns: Optional[role_summary_status.RoleSummaryStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[role_summary_status.RoleSummaryStatus] = None) -> None:
        """
        Sets the status property value. Possible values are: ok, bad. The value depends on the ratio of (managedCount / usersCount). If the ratio is less than a predefined threshold, ok is returned. Otherwise, bad is returned.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def users_count(self,) -> Optional[int]:
        """
        Gets the usersCount property value. The number of users that are assigned with the role.
        Returns: Optional[int]
        """
        return self._users_count
    
    @users_count.setter
    def users_count(self,value: Optional[int] = None) -> None:
        """
        Sets the usersCount property value. The number of users that are assigned with the role.
        Args:
            value: Value to set for the usersCount property.
        """
        self._users_count = value
    

