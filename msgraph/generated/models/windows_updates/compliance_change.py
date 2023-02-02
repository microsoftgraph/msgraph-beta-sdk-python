from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
update_policy = lazy_import('msgraph.generated.models.windows_updates.update_policy')

class ComplianceChange(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new complianceChange and sets the default values.
        """
        super().__init__()
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The isRevoked property
        self._is_revoked: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The revokedDateTime property
        self._revoked_date_time: Optional[datetime] = None
        # The updatePolicy property
        self._update_policy: Optional[update_policy.UpdatePolicy] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ComplianceChange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ComplianceChange
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ComplianceChange()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "isRevoked": lambda n : setattr(self, 'is_revoked', n.get_bool_value()),
            "revokedDateTime": lambda n : setattr(self, 'revoked_date_time', n.get_datetime_value()),
            "updatePolicy": lambda n : setattr(self, 'update_policy', n.get_object_value(update_policy.UpdatePolicy)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_revoked(self,) -> Optional[bool]:
        """
        Gets the isRevoked property value. The isRevoked property
        Returns: Optional[bool]
        """
        return self._is_revoked
    
    @is_revoked.setter
    def is_revoked(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRevoked property value. The isRevoked property
        Args:
            value: Value to set for the is_revoked property.
        """
        self._is_revoked = value
    
    @property
    def revoked_date_time(self,) -> Optional[datetime]:
        """
        Gets the revokedDateTime property value. The revokedDateTime property
        Returns: Optional[datetime]
        """
        return self._revoked_date_time
    
    @revoked_date_time.setter
    def revoked_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the revokedDateTime property value. The revokedDateTime property
        Args:
            value: Value to set for the revoked_date_time property.
        """
        self._revoked_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_bool_value("isRevoked", self.is_revoked)
        writer.write_datetime_value("revokedDateTime", self.revoked_date_time)
        writer.write_object_value("updatePolicy", self.update_policy)
    
    @property
    def update_policy(self,) -> Optional[update_policy.UpdatePolicy]:
        """
        Gets the updatePolicy property value. The updatePolicy property
        Returns: Optional[update_policy.UpdatePolicy]
        """
        return self._update_policy
    
    @update_policy.setter
    def update_policy(self,value: Optional[update_policy.UpdatePolicy] = None) -> None:
        """
        Sets the updatePolicy property value. The updatePolicy property
        Args:
            value: Value to set for the update_policy property.
        """
        self._update_policy = value
    

