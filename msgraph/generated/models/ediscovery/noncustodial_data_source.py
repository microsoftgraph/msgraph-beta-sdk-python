from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .data_source import DataSource
    from .data_source_container import DataSourceContainer

from .data_source_container import DataSourceContainer

@dataclass
class NoncustodialDataSource(DataSourceContainer):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.ediscovery.noncustodialDataSource"
    # Indicates if hold is applied to noncustodial data source (such as mailbox or site).
    apply_hold_to_source: Optional[bool] = None
    # User source or SharePoint site data source as noncustodial data source.
    data_source: Optional[DataSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NoncustodialDataSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NoncustodialDataSource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return NoncustodialDataSource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .data_source import DataSource
        from .data_source_container import DataSourceContainer

        from .data_source import DataSource
        from .data_source_container import DataSourceContainer

        fields: Dict[str, Callable[[Any], None]] = {
            "applyHoldToSource": lambda n : setattr(self, 'apply_hold_to_source', n.get_bool_value()),
            "dataSource": lambda n : setattr(self, 'data_source', n.get_object_value(DataSource)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("applyHoldToSource", self.apply_hold_to_source)
        writer.write_object_value("dataSource", self.data_source)
    

