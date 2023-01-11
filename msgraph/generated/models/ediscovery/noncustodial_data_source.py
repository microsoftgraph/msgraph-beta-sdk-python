from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

data_source = lazy_import('msgraph.generated.models.ediscovery.data_source')
data_source_container = lazy_import('msgraph.generated.models.ediscovery.data_source_container')

class NoncustodialDataSource(data_source_container.DataSourceContainer):
    @property
    def apply_hold_to_source(self,) -> Optional[bool]:
        """
        Gets the applyHoldToSource property value. Indicates if hold is applied to non-custodial data source (such as mailbox or site).
        Returns: Optional[bool]
        """
        return self._apply_hold_to_source
    
    @apply_hold_to_source.setter
    def apply_hold_to_source(self,value: Optional[bool] = None) -> None:
        """
        Sets the applyHoldToSource property value. Indicates if hold is applied to non-custodial data source (such as mailbox or site).
        Args:
            value: Value to set for the applyHoldToSource property.
        """
        self._apply_hold_to_source = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new NoncustodialDataSource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.ediscovery.noncustodialDataSource"
        # Indicates if hold is applied to non-custodial data source (such as mailbox or site).
        self._apply_hold_to_source: Optional[bool] = None
        # User source or SharePoint site data source as non-custodial data source.
        self._data_source: Optional[data_source.DataSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NoncustodialDataSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NoncustodialDataSource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NoncustodialDataSource()
    
    @property
    def data_source(self,) -> Optional[data_source.DataSource]:
        """
        Gets the dataSource property value. User source or SharePoint site data source as non-custodial data source.
        Returns: Optional[data_source.DataSource]
        """
        return self._data_source
    
    @data_source.setter
    def data_source(self,value: Optional[data_source.DataSource] = None) -> None:
        """
        Sets the dataSource property value. User source or SharePoint site data source as non-custodial data source.
        Args:
            value: Value to set for the dataSource property.
        """
        self._data_source = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "apply_hold_to_source": lambda n : setattr(self, 'apply_hold_to_source', n.get_bool_value()),
            "data_source": lambda n : setattr(self, 'data_source', n.get_object_value(data_source.DataSource)),
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
        writer.write_bool_value("applyHoldToSource", self.apply_hold_to_source)
        writer.write_object_value("dataSource", self.data_source)
    

