from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_configuration_schema_request_detail import AppConfigurationSchemaRequestDetail

from .app_configuration_schema_request_detail import AppConfigurationSchemaRequestDetail

@dataclass
class ManagedStoreAppConfigurationSchemaRequestDetail(AppConfigurationSchemaRequestDetail, Parsable):
    """
    The request parameter for requesting Android Managed Play Store app configuration schema.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.managedStoreAppConfigurationSchemaRequestDetail"
    # The package name of the Android Managed Play Store app
    package_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedStoreAppConfigurationSchemaRequestDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedStoreAppConfigurationSchemaRequestDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedStoreAppConfigurationSchemaRequestDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_configuration_schema_request_detail import AppConfigurationSchemaRequestDetail

        from .app_configuration_schema_request_detail import AppConfigurationSchemaRequestDetail

        fields: dict[str, Callable[[Any], None]] = {
            "packageName": lambda n : setattr(self, 'package_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("packageName", self.package_name)
    

