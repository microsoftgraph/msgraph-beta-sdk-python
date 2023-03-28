from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import content_approval, update_policy
    from .. import entity

from .. import entity

class ComplianceChange(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new complianceChange and sets the default values.
        """
        super().__init__()
        # The date and time when a compliance change was created.
        self._created_date_time: Optional[datetime] = None
        # True indicates that a compliance change is revoked, preventing further application. Revoking a compliance change is a final action.
        self._is_revoked: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The date and time when the compliance change was revoked.
        self._revoked_date_time: Optional[datetime] = None
        # The policy this compliance change is a member of.
        self._update_policy: Optional[update_policy.UpdatePolicy] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when a compliance change was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when a compliance change was created.
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
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.windowsUpdates.contentApproval":
                from . import content_approval

                return content_approval.ContentApproval()
        return ComplianceChange()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import content_approval, update_policy
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
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
        Gets the isRevoked property value. True indicates that a compliance change is revoked, preventing further application. Revoking a compliance change is a final action.
        Returns: Optional[bool]
        """
        return self._is_revoked
    
    @is_revoked.setter
    def is_revoked(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRevoked property value. True indicates that a compliance change is revoked, preventing further application. Revoking a compliance change is a final action.
        Args:
            value: Value to set for the is_revoked property.
        """
        self._is_revoked = value
    
    @property
    def revoked_date_time(self,) -> Optional[datetime]:
        """
        Gets the revokedDateTime property value. The date and time when the compliance change was revoked.
        Returns: Optional[datetime]
        """
        return self._revoked_date_time
    
    @revoked_date_time.setter
    def revoked_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the revokedDateTime property value. The date and time when the compliance change was revoked.
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
        Gets the updatePolicy property value. The policy this compliance change is a member of.
        Returns: Optional[update_policy.UpdatePolicy]
        """
        return self._update_policy
    
    @update_policy.setter
    def update_policy(self,value: Optional[update_policy.UpdatePolicy] = None) -> None:
        """
        Sets the updatePolicy property value. The policy this compliance change is a member of.
        Args:
            value: Value to set for the update_policy property.
        """
        self._update_policy = value
    

