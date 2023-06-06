from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .. import custom_callout_extension, custom_extension_callback_configuration, user

from .. import custom_callout_extension

@dataclass
class CustomTaskExtension(custom_callout_extension.CustomCalloutExtension):
    odata_type = "#microsoft.graph.identityGovernance.customTaskExtension"
    # The callback configuration for a custom task extension.
    callback_configuration: Optional[custom_extension_callback_configuration.CustomExtensionCallbackConfiguration] = None
    # The unique identifier of the Azure AD user that created the custom task extension.Supports $filter(eq, ne) and $expand.
    created_by: Optional[user.User] = None
    # When the custom task extension was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    created_date_time: Optional[datetime] = None
    # The unique identifier of the Azure AD user that modified the custom task extension last.Supports $filter(eq, ne) and $expand.
    last_modified_by: Optional[user.User] = None
    # When the custom extension was last modified.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    last_modified_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomTaskExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomTaskExtension
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomTaskExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .. import custom_callout_extension, custom_extension_callback_configuration, user

        fields: Dict[str, Callable[[Any], None]] = {
            "callbackConfiguration": lambda n : setattr(self, 'callback_configuration', n.get_object_value(custom_extension_callback_configuration.CustomExtensionCallbackConfiguration)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(user.User)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(user.User)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("callbackConfiguration", self.callback_configuration)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

