from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UsageRightsInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates whether the user has permission to copy content from the protected resource. When true, copying is allowed; when false, copying is restricted by the sensitivity label policy.
    allow_copy: Optional[bool] = None
    # Indicates whether the user has permission to edit or modify the protected content. When true, editing is allowed; when false, the content is read-only for this user.
    allow_edit: Optional[bool] = None
    # Indicates whether the user has permission to export or save the protected content to external locations. When true, exporting is allowed; when false, export operations are restricted.
    allow_export: Optional[bool] = None
    # Indicates whether the user has permission to print the protected content. When true, printing is allowed; when false, print functionality is disabled.
    allow_print: Optional[bool] = None
    # Indicates whether the user has permission to view or access the protected content. When true, the user can view the content; when false, access is denied.
    allow_view: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UsageRightsInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UsageRightsInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UsageRightsInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allowCopy": lambda n : setattr(self, 'allow_copy', n.get_bool_value()),
            "allowEdit": lambda n : setattr(self, 'allow_edit', n.get_bool_value()),
            "allowExport": lambda n : setattr(self, 'allow_export', n.get_bool_value()),
            "allowPrint": lambda n : setattr(self, 'allow_print', n.get_bool_value()),
            "allowView": lambda n : setattr(self, 'allow_view', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("allowCopy", self.allow_copy)
        writer.write_bool_value("allowEdit", self.allow_edit)
        writer.write_bool_value("allowExport", self.allow_export)
        writer.write_bool_value("allowPrint", self.allow_print)
        writer.write_bool_value("allowView", self.allow_view)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

